# Google OAuth 2.0 and OAuth consent screen

# authetication to google api services
# create oauth client secret file

# https://console.cloud.google.com/

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1-189Vhax_EWg1EpywaxbIBIiQCxpZTvp'

file1 = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : 'something1.csv'})
file1.SetContentString('Hello world!, this is my second file')
file1.Upload()

# Upload files to google drive
# List files in google drive
# Download files from google drive
'''
directory = "/home/a3logics/Downloads/pythonProject/GoogleDriveCsv/data"
for f in os.listdir(directory):
    filename = os.path.join(directory, f)
    gfile = drive.CreateFile({'parents': [{'id': folder}], 'title': f})
    gfile.SetContentFile(filename)
    gfile.Upload()
    print(filename)
    print(f)

# Download files
file_list = drive.ListFile({'q': f"'{folder}' in parents and trashed=false"}).GetList()
for index, file in enumerate(file_list):
    print(index + 1, 'file downloaded : ', file['title'])
    file.GetContentFile(file['title']) '''