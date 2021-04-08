pip install paramiko 
pip install pyperclip 
pip install win10toast 
pushd %~dp0
set script_dir=%CD%
py install.py
install.reg
pause