# EdShare
Share quickly file from Windows Right Click to web site using SSH. Program upload file to web server then give url for download. [See demonstration](https://github.com/EnzoDeg40/EdShare/blob/main/demo.gif).

![Windows Right Click](rightclick.png)

Requirements:
* Web server with SSH acces 
* Windows client
* [Python 3](https://python.org/)
* Packages Python `pip install paramiko pyperclip win10toast`

Installation:
* Download this repository
* Put the folder in the desired location for installation
* Open `install.bat` with administrator rights
* Modify variables in `main.py`

Usage:
* Open Windows explorer
* Make a right click on file
* Select `EdShare` to upload file to your server

![Windows Demonstration](demo.gif)

Note:
* If folder has moved, reopen `install.bat` to update path of program

Uninstallation : 
* Open `uninstall.reg`

