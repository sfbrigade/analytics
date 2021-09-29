"""
This script uses the slack users.list endpoint to pull
all users.

Refer to https://api.slack.com/methods/users.list
"""

import os
import logging
import pandas as pd
from slack_sdk import WebClient  # Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)


"""
FUNCTIONS
"""
def connect(api_token):
    """ Executes request via Slack SDK and returns json"""
    client = WebClient(token = api_token)
    logger = logging.getLogger(__name__)
    response = client.users_list()

    return response


def format_users_list(response):
    """ Formats conversation list and creates dataframe """

    user_list = []

    for i in response["members"]:
        user_list.append({
             "id": i.get("id"),
             "email": i["profile"].get("email"),
             "title": i["profile"].get("title"),
             "first_name": i["profile"].get("first_name"),
             "last_name": i["profile"].get("last_name"),
             "real_name": i["profile"].get("real_name"),
             "tz": i["profile"].get("tz"),
             "display_name": i["profile"].get("display_name"),
             "is_email_confirmed": i["profile"].get("is_email_confirmed"),
             "updated": i["profile"].get("updated")
             }
             )

        user_list_data = pd.DataFrame(user_list)

    return user_list_data


"""
MAIN
"""
def main():

    C4SF_SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN')

    # Connect to slack and get users_list
    response = connect(C4SF_SLACK_API_TOKEN)

    # Make destination directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Format Users List and export to csv
    user_list_data = format_users_list(response)
    user_list_data.to_csv('data/user_list_data.csv')



main()



