"""
This pull will take appx 30 minutes given the rate limit (appx 200 rows/s)

This script uses the slack conversations.history endpoint to pull
all public messages in historical or archived channels.

Refer to https://api.slack.com/methods/conversations.history
"""


import os
import logging
import pandas as pd
from slack_sdk import WebClient  # Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
import time


"""
FUNCTIONS
"""
def connect(api_token, endpoint):
    # Initiate Client
    client = WebClient(token=api_token)
    logger = logging.getLogger(__name__)
    response = eval(endpoint)

    return response





def format_conversations_list(response):
    """
    Formats conversation list.

    :param response:
    :return:
    """
    # Capture slack channels
    #response = connect(C4SF_SLACK_API_TOKEN, 'client.conversations_list(limit = 10)')

    conversation_list_data = pd.json_normalize(response['channels'])

    # conversation_list_data['created'] = pd.to_datetime(conversation_list_data['created'], unit='s')

    conversation_list_data = conversation_list_data[
        [
            'id'
            , 'name'
            , 'created'
            , 'is_archived'
            , 'is_shared'
            , 'creator'
            , 'is_group'
            , 'is_im'
            , 'is_private'
            , 'is_ext_shared'
            , 'is_org_shared'
            , 'num_members'
            , 'topic.value'
            , 'topic.creator'
            , 'topic.last_set'
            , 'purpose.value'
            , 'purpose.creator'
            , 'purpose.last_set'
        ]]

    return conversation_list_data



"""
MAIN
"""
def main():

    C4SF_SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN')

    # Connect to slack and get users_list
    response = connect(C4SF_SLACK_API_TOKEN, 'client.conversations_list(limit = 1000)')

    # Format Users List and export to csv
    conversations_list_data = format_conversations_list(response)


    messages=[]


    for channel in conversations_list_data["id"]:

        cursor=""
        df = pd.DataFrame()
        has_more = True

        # Continue processing through all pages
        while has_more == True:

            # If request fails, retry up to 10 times


            response = connect(C4SF_SLACK_API_TOKEN, 'client.conversations_history(cursor="'+ cursor + '", limit = 200, channel = "'+ channel + '")')

            # Populate next page
            has_more = response["has_more"]
            if has_more == True:
                cursor = response["response_metadata"]["next_cursor"]



            messages_batch = []

            # Schema is inconsistent in data, so need to standardize data for each batch
            for i in response["messages"]:
                messages.append({
                    "channel": channel,
                    "type": i.get("type"),
                    "user": i.get("user"),
                    "text": i.get("text"),
                    "ts": i.get("ts"),
                }
                )

            messages.append(messages_batch)
            print(len(messages))

            # Sleep to avoid hitting rate limit (50 requests / min)
            time.sleep(1)


        # Make a data frame with the columns we need and export to csv
        messages_data = pd.DataFrame(messages, columns = ['channel', 'type','user', 'text', 'ts'])
        messages_data['ts'] = pd.to_datetime(messages_data['ts'], unit='s')

    # Make destination directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    messages_data.to_csv('data/conversations_history.csv')

main()



# TODO: Look into error handling and retrying each batch if it fails
#   See https://echohack.medium.com/patterns-with-python-poll-an-api-832173a03e93
