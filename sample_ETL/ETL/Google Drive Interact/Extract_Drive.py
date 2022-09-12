from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# this 2 line will get the information in Setting.yaml
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Folder from google drive you want to upload file
targetDirID = '1Ry7QF4coPXHgX7RwrGEc5hFal-Hz2IHo'

targetLocation = os.path.join(os.getcwd(), '/Data From Google/')
list_file = ['Table3.xlsx', 'Table3.Exports June 2021.csv']

# List all file in this folder on Google Drive
exist_file_list = drive.ListFile(
    {'q': "'{}' in parents and trashed=false".format(targetDirID)}).GetList()

for file in exist_file_list:
    if file['title'] in list_file:
        full_path = targetLocation + file['title']
        file1 = drive.CreateFile({'id': file['id']})
        print('Downloading file %s from Google Drive' % file1['title'])
        file1.GetContentFile('{}/Data From Google/{}'.format(os.getcwd(), file['title']))