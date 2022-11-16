"""
Export files to pydrive

Files must be listed in scope on google api console:
https://console.cloud.google.com/apis/credentials/consent/edit;newAppInternalUser=true?authuser=1&project=code-for-sf-data-pipeline&supportedpurview=project 


Resource: https://www.projectpro.io/recipes/upload-files-to-google-drive-using-python
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  


"""
upload_file_list = ['../data/conversation_list_data.csv']
for upload_file in upload_file_list:
    gfile = drive.CreateFile({'parents': [{'id': '1I22OJqV8N3EmKH54NUnjq8HPFruKpc74-t'}]})
    # Read file and set it as the content of this instance.
    gfile.SetContentFile(upload_file)
    gfile.Upload() # Upload the file.
"""
file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1I22OJqV8N3EmKH54NUnjq8HPFruKpc74')}).GetList()
for file in file_list:
    print('title: %s, id: %s' % (file['title'], file['id']))

# Client ID: 806142411127-vvtfurhp0osml8gqdkdtknsr70uio1kk.apps.googleusercontent.com
# Client Secret: "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"