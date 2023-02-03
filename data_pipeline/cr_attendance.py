"""
This script uses the airtable api to pull attendance info

https://airtable.com/appS8zufRQWdMERuO/api/docs#curl/authentication
https://pyairtable.readthedocs.io/en/latest/getting-started.html
"""

import os
import pandas as pd
from pyairtable import Table

api_key = os.getenv('AIRTABLE_API_KEY')
base = 'appS8zufRQWdMERuO'
table ='Attendance'
response = Table(api_key, base, table)

# Iterate and return all records, format to DataFrame
response = response.all()

attendance_batch = []

# Convert json to denormalized table
for i in response:
    attendance_batch.append({
    "createdTime": i.get("createdTime"),
    "email": i["fields"].get("Email"),
    "date": i["fields"].get("WDate"),
    "whyAttend": i["fields"].get("What brings you here?"),
    "productName": i["fields"].get("Product Name")
    })

attendance_batch = pd.DataFrame(attendance_batch)

attendance_batch.to_csv('../data/attendance.csv')

print('Attendance records processed')


