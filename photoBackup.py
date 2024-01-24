from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import datetime

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

PhotoBackupFolderPath = '1RN3ZXzeNV9iam7skUVPF3oWNvyEx7b23'


# this part creates 'Backup Completed.txt' file in drive indicating that download has been successful
backupFinishFile = drive.CreateFile({
    'parents': [{
        'id': PhotoBackupFolderPath}],
        'title': 'Backup Completed.txt' 
    })

#Content of 'Backup Completed.txt' stating the status
currentDate =  datetime.datetime.now()
strDate = str(currentDate) 
s = {
    "Status" : "Successfully Downloaded",
    "Current_Date" : strDate,
}

backupFinishFile.SetContentString(s)
backupFinishFile.Upload()