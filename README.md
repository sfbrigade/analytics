# Overview
We're working to make every step of the Code for SF experience great, from finding your first project to making your first contribution.

# Goals / Scope
The goal of this project is to build an understanding of member engagement and diversity with Code for San Francisco.

# How to contribute

- You can find open issues here: https://github.com/sfbrigade/analytics


# Roles
- Product Owner (Greg)
- Project Coordinator (Ti)
- Data Scientists (Rocky)

Looking for Data Scientists
Critical Thinkers

# How to Get Started

## For creating workbooks:
1. Request permission from Greg to google drive that has data already available
2. Create a local repository via github (or GitHub Desktop)
3. Add files to the folder called "data" for organization.
4. Create workbooks in the folder called "workbooks" for organization.

# Available Raw Data
user_list_data -> A list of all the users in our slack community
conversation_list_data -> A list of all channels in our slack community
conversations_history_data -> A list of all the public messages in our slack community
members -> A list of members and demographic information
attendance -> A list of attendance information

## For processing data yourself
=======
1.  Ensure Pip is updated (some packages may fail otherwise):
	```
	pip3 install --upgrade pip
	```
2.  Create and activate a virtual environment by running this in terminal (and install virtualenv if needed):
    ```
    pip3 install virtualenv

    python3 -m venv venv
    ```
3.  Set up local environmnetal variables. There are 2 api keys, one for slack and one for airtable that need to be added to the end of the file "venv/bin/activate". This is the environment config file that is run when you activate your virtual environment.

4.  Activate virtual environment by navigating to your local report and running:
	```
	source venv/bin/activate
	```

5. Run requirements.txt so that you have all of the proper packages:
	```
	pip install -r requirements.txt
	```



- New here? Here's the link to the project history on Notion: #Use Notion, what is best practice for catching up from 0?
- https://www.notion.so/sfbrigade/Analytics-60a30e72aa8846649a3e2539796c8ff6






