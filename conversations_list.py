import os
import logging
import pandas as pd
from slack_sdk import WebClient  # Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)


"""
FUNCTIONS
"""
def connect(api_token):
    """
    Executes request via Slack SDK

    :param api_token: API token associated with the request
    :param limit: The number of records returned. 1000 is the max allowed and more than sufficient.
    :return: Response: The json package from Slack
    """
    client = WebClient(token=api_token)
    logger = logging.getLogger(__name__)
    response = client.conversations_list(limit=1000)

    return response



def format_conversations_list(response):
    """ Formats conversation list and creates dataframe """

    conversation_list_data = pd.json_normalize(response['channels'])

    # Format timestamps
    conversation_list_data['created'] = pd.to_datetime(conversation_list_data['created'], unit='s')
    conversation_list_data['purpose.last_set'] = pd.to_datetime(conversation_list_data['purpose.last_set'], unit='s')
    conversation_list_data['topic.last_set'] = pd.to_datetime(conversation_list_data['topic.last_set'], unit='s')

    # Limits the columns returned to those used for analysis
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
    response = connect(api_token=C4SF_SLACK_API_TOKEN)

    # Make destination directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Format Users List and export to csv
    conversations_list_data = format_conversations_list(response)
    conversations_list_data.to_csv('data/conversation_list_data.csv')

main()



