import os
import logging
import pandas as pd
from slack_sdk import WebClient  # Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)


"""
FUNCTIONS
"""
def connect(api_token, endpoint):
    # Initiate Client
    client = WebClient(token=api_token)
    logger = logging.getLogger(__name__)
    response = eval(endpoint)

    return response


# Refer to https://api.slack.com/methods/users.list
# response = connect(C4SF_SLACK_API_TOKEN,'client.users_list()')



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

    # Make destination directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    conversations_list_data.to_csv('conversation_list_data.csv')



main()



