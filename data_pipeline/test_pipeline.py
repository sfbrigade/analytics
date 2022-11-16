"""
Pytest cases for data pipeline
"""
import os
from conversations_list import *
from users_list import *

def test_slack_connection():
    C4SF_SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN')
    connect(api_token=C4SF_SLACK_API_TOKEN)


# TODO Improve testing, validate response
# https://python.plainenglish.io/how-to-validate-your-dataframes-with-pytest-b238d2891d12

def test_format_conversations_list():

    # Example expected response
    response = {'ok': True
        , 'channels': 
            [
                {'id': 'C0431NL8L', 'name': 'general', 'is_channel': True, 'is_group': False, 'is_im': False, 'is_mpim': False, 'is_private': False, 'created': 1426741076, 'is_archived': False, 'is_general': True, 'unlinked': 0, 'name_normalized': 'general', 'is_shared': False, 'is_org_shared': False, 'is_pending_ext_shared': False, 'pending_shared': [], 'context_team_id': 'T0431NL8C', 'updated': 1558180400615, 'parent_conversation': None, 'creator': 'U0431NL8E', 'is_ext_shared': False, 'shared_team_ids': ['T0431NL8C'], 'pending_connected_team_ids': [], 'is_member': True, 'topic': {'value': 'Agenda: <http://c4sf.me/agenda|c4sf.me/agenda>. Contact the organizing team via <!subteam^S2B87KLEM|@coreteam>.', 'creator': 'U88CNUHF0', 'last_set': 1553131688}, 'purpose': {'value': 'This channel is for team-wide communication and announcements. All team members are in this channel. &lt;a href="https://docs.google.com/document/d/1ZV_iy2CeDlTu13Af9-_5NyOC8SVP9mpxIBn0g1e_S-Q/edit"&gt;Code of Conduct&lt;/a&gt;', 'creator': 'U0431NL8E', 'last_set': 1439431590}, 'previous_names': [], 'num_members': 3904}, {'id': 'C0431NL8N', 'name': 'random', 'is_channel': True, 'is_group': False, 'is_im': False, 'is_mpim': False, 'is_private': False, 'created': 1426741076, 'is_archived': False, 'is_general': False, 'unlinked': 0, 'name_normalized': 'random', 'is_shared': False, 'is_org_shared': False, 'is_pending_ext_shared': False, 'pending_shared': [], 'context_team_id': 'T0431NL8C', 'updated': 1558180400621, 'parent_conversation': None, 'creator': 'U0431NL8E', 'is_ext_shared': False, 'shared_team_ids': ['T0431NL8C'], 'pending_connected_team_ids': [], 'is_member': True, 'topic': {'value': '', 'creator': '', 'last_set': 0}, 'purpose': {'value': "A place for non-work-related flimflam, hodge-podge or jibber-jabber you'd prefer to keep out of more focused work-related channels.", 'creator': 'U043262MY', 'last_set': 1439752214}, 'previous_names': [], 'num_members': 3821}, {'id': 'C043CH4AH', 'name': 'newsletter-stuff', 'is_channel': True, 'is_group': False, 'is_im': False, 'is_mpim': False, 'is_private': False, 'created': 1426817253, 'is_archived': True, 'is_general': False, 'unlinked': 0, 'name_normalized': 'newsletter-stuff', 'is_shared': False, 'is_org_shared': False, 'is_pending_ext_shared': False, 'pending_shared': [], 'context_team_id': 'T0431NL8C', 'updated': 1590167026715, 'parent_conversation': None, 'creator': 'U043F5GFW', 'is_ext_shared': False, 'shared_team_ids': ['T0431NL8C'], 'pending_connected_team_ids': [], 'is_member': False, 'topic': {'value': '', 'creator': '', 'last_set': 0}, 'purpose': {'value': 'This is where everything related to the newsletter should be put. Right here!', 'creator': 'U043F5GFW', 'last_set': 1426817253}, 'previous_names': [], 'num_members': 0}, 
            ]
        , 'response_metadata': {'next_cursor': ''}
        }

    assert not format_conversations_list(response).empty
