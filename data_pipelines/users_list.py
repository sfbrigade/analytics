"""
This script uses the slack users.list endpoint to pull
all users.

Refer to https://api.slack.com/methods/users.list
"""

import os
import logging
import pandas as pd
import time
import pdb
from slack_sdk import WebClient  # Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)


"""
FUNCTIONS
"""
def connect(api_token, endpoint):
    """ Executes request via Slack SDK and returns json"""
    client = WebClient(token=api_token)
    logger = logging.getLogger(__name__)
    response = eval(endpoint)

    return response


def format_users_list(api_token):
    """ Formats conversation list and creates dataframe """

    tries = 0
    delay = 1
    while tries < 10:
        try:
            #C4SF_SLACK_API_TOKEN
            response = connect(api_token, endpoint='client.users_list(limit = 200)')
            time.sleep(delay)
            break
        except Exception as e:
            tries += 1
            delay *= 2
            print('{}, retry with {}s delay'.format(e,delay))
               
    cursor = response["response_metadata"]["next_cursor"]


    users = []

    users_batch = []

    for i in response["members"]:
        users_batch.append({
             "id": i.get("id"),
             "email": i["profile"].get("email"),
             "title": i["profile"].get("title"),
             "first_name": i["profile"].get("first_name"),
             "last_name": i["profile"].get("last_name"),
             "real_name": i["profile"].get("real_name"),
             "tz": i["profile"].get("tz"),
             "display_name": i["profile"].get("display_name"),
             "is_email_confirmed": i["profile"].get("is_email_confirmed"),
             "updated": i["profile"].get("updated"),
             }
             )

    users.extend(users_batch)

    # Continue processing through all pages
    tries = 0
    while cursor != "" and tries < 10:

        # If request fails, retry up to 10 times
        tries = 0
        delay = 1

        while tries < 10:
            try:
                response = connect(api_token, endpoint='client.users_list(cursor="'+ cursor + '", limit = 200)')
                time.sleep(delay)
        
                break
            except Exception as e:
                tries += 1
                delay *= 2
                print('{}, retry with {}s delay'.format(e,delay))
           

        # Populate next page
        cursor = response["response_metadata"]["next_cursor"]
        

        test_response = pd.json_normalize(response['members'])

        users_batch = []

        for i in response["members"]:
            users_batch.append({
                 "id": i.get("id"),
                 "email": i["profile"].get("email"),
                 "title": i["profile"].get("title"),
                 "first_name": i["profile"].get("first_name"),
                 "last_name": i["profile"].get("last_name"),
                 "real_name": i["profile"].get("real_name"),
                 "tz": i["profile"].get("tz"),
                 "display_name": i["profile"].get("display_name"),
                 "is_email_confirmed": i["profile"].get("is_email_confirmed"),
                 "updated": i["profile"].get("updated"),
                 }
                 )

        # users_batch works
        
        users.extend(users_batch)

        print(len(users), 'records processed')

    user_list_data = pd.DataFrame(users) 

    return user_list_data

###################################
###################################
###################################
"""
MAIN
"""
def main():

    # Connect to slack and get users_list
    C4SF_SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN')

    # Format Users List and export to csv
    user_list_data = format_users_list(C4SF_SLACK_API_TOKEN)

    # Make destination directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Format Users List and export to csv
    user_list_data.to_csv('data/user_list_data.csv')
    print('success')

    
main()



