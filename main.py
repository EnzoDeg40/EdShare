import sys
import os
import paramiko
import pyperclip
from win10toast import ToastNotifier



# SSH connection
sshSrv = '' # IP of ssh server
sshUsr = '' # Username
sshPwd = '' # Password 
sshPor = '' # Port

publicUrl = '' #eg https://mysite.com/uploads/
serverPath = '' #eg /var/www/html/uploads/

notification = True
clipboard = True
lang = 'fr' # 'fr' or 'en'
notificationDuration = 3



# Get argument
filePath = str(sys.argv[1]) 

if filePath.find('\\') > -1:
    fileName = filePath.split('\\')[-1]
else:
    fileName = filePath

# Initiate SSH connection
ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=sshSrv, username=sshUsr, password=sshPwd, port=sshPor)

# Initiate SFTP connection
sftp = ssh.open_sftp()
# Send file to the server without space
sftp.put(filePath, serverPath + fileName.replace(' ', '_'))

# Close connection
sftp.close()
ssh.close()

# Copie l'url du fichier si la valeur est vrai
if clipboard:
    pyperclip.copy(publicUrl + fileName.replace(' ', '_'))

# Affiche une notifcation windows si la valeur est vrai
if lang == 'fr':
    notificationTitle = 'Fichier publié'
    notificationText = 'Le fichier est prêt à être partagé'
else:
    notificationTitle = 'File shared'
    notificationText = 'File is ready to be share'

if notification:
    toaster = ToastNotifier()
    toaster.show_toast(notificationTitle, notificationText, icon_path="C:\EdShare/nitro.ico", duration=notificationDuration)