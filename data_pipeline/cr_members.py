"""
This script uses the airtable api to pull member info

https://airtable.com/appS8zufRQWdMERuO/api/docs#curl/authentication
https://pyairtable.readthedocs.io/en/latest/getting-started.html
"""
import os
import pandas as pd
from pyairtable import Table

api_key = os.getenv('AIRTABLE_API_KEY')
base = 'appS8zufRQWdMERuO'
table ='Members'
response = Table(api_key, base, table)

# Iterate and return all records, format to DataFrame
response = response.all()

member_batch = []

# Convert json to denormalized table
for i in response:
    member_batch.append({
    "createdTime": i.get("createdTime"),
    "profession": i["fields"].get("What is your profession?"),
    "income": i["fields"].get("Income"),
    "emailAddress": i["fields"].get("Email Address"),
    "raceEthnicity": i["fields"].get("Race/Ethnicity"),
    "gender": i["fields"].get("Gender"),
    "ageRange": i["fields"].get("Age Range"),
    "fullName": i["fields"].get("What is your Full Name?"),
    "whatBrought": i["fields"].get("What brought you to Code for San Francisco?"),
    "areasInterest": i["fields"].get("Areas of Interest"),
    "howInvovled": i["fields"].get("How do you want to get involved? "),
    "interestedRoles": i["fields"].get("What roles are you interested in at Code for San Francisco? "),
    "techStack": i["fields"].get("Tech Stack"),
    "profession": i["fields"].get("What is your profession"),
    "experience": i["fields"].get("Experience Level")   
    })

member_batch = pd.DataFrame(member_batch)

member_batch.to_csv('../data/members.csv')


print('Members list processed')




