
# Scrpit to test PyDrive2 to see if it can find the file
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Test listing one file
file_list = drive.ListFile({'q': 'trashed=false', 'maxResults': 1}).GetList()
for f in file_list:
    print(f['title'])
