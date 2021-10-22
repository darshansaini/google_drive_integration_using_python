from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


import json
import requests
headers = {"Authorization": "Bearer ya29.a0ARrdaM8i4T_Su0Z-nnjKxctRl_0oQ14N-x70gE-ZYrFy1wyJZjoZ3lrPn2jFREGyr747XNg62Iridd8TaY-okg6vrH3BPNuhnj1BKMT8KA-X4Qz0HBG4pyyGF5d00XhIs8LV96rhYmkAUeDOFUh052SKst7p"} #put ur access token after the word 'Bearer '
para = {
    "name": "something.csv", #file name to be uploaded
    "parents": ["1-189Vhax_EWg1EpywaxbIBIiQCxpZTvp"] # make a folder on drive in which you want to upload files; then open that folder; the last thing in present url will be folder id
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': ('text/csv',open("./something.csv", "rb")) 
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
