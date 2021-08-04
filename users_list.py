import os
import logging
import pandas as pd
from slack_sdk import WebClient # Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)

C4SF_SLACK_API_TOKEN= os.getenv('SLACK_API_TOKEN')

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



#%%
# This method is required rather than json_normalize. It accounts for fields that may not be included in
# the first row (such as profile.update, which would not return using json_normalize)

def format_users_list(response):
    """
    Formats user list.

    This method is required rather than json_normalize. It accounts for fields that may not be included in
    the first row (such as profile.update, which would not return using json_normalize). This should be validated as an understanding of the data.

    :param response:
    :return:
    """
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

# Write Results to CSV
#channels_data = result["members"]
#channels_data_flat = pd.json_normalize(channels_data, 'id')
#channels_data_flat['created'] = pd.to_datetime(channels_data_flat['created'], unit='s')
#channels_data_flat.to_csv('slack_channels_final.csv')




"""
MAIN
"""
def main():
    # Connect to slack and get users_list
    response = connect(C4SF_SLACK_API_TOKEN, 'client.users_list()')

    # Format Users List and export to csv
    user_list_data = format_users_list(response)

    user_list_data.to_csv('user_list_data.csv')

main()