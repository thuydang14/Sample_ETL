from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# this 2 line will get the information in Setting.yaml
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Folder from google drive you want to upload file
targetDirID = '1Ry7QF4coPXHgX7RwrGEc5hFal-Hz2IHo'

location_path = os.path.join(os.getcwd(), '../../Data')


list_file = ['Table3.xlsx', 'Table3.Exports June 2021.csv']

# List all file in this folder on Google Drive
exist_file_list = drive.ListFile(
    {'q': "'{}' in parents and trashed=false".format(targetDirID)}).GetList()

for file in list_file:
    if not os.path.exists(f'{location_path}/{file}'):
        continue

    fileName = os.path.basename(f'{location_path}/{file}')
    for namefile in exist_file_list:
        if namefile['title'] == fileName:
            namefile.Delete()

    gfile = drive.CreateFile(
        {'parents': [{'id': targetDirID}], 'title': fileName})
    # Read file and set it as the content of this instance
    gfile.SetContentFile(f'{location_path}/{file}')
    gfile.Upload()  # upload the file
