import os

folder = os.getcwd()

print("EdShare installer")
print("Ne déplacer pas le dossier après l'installation")
print("Dossier d'installation :", os.getcwd())

r = input(colored("Continuer l'installation (O/n) ? ", 'yellow'))

if r.lower() == 'o' or r == '':

    print("Ecriture du fichier d'installation au registre...")

    r = '\n'

    # Clear file
    f = open('install.reg', 'w')
    f.write('')
    f.close

    # Create install file
    f = open('install.reg', 'a')

    f.write('Windows Registry Editor Version 5.00' + r)
    f.write(r)
    f.write('[HKEY_CLASSES_ROOT\*\shell\EdShare]' + r)
    f.write(r'"Icon"="\"' + folder.replace("\\", "\\\\") + r'\\icon.ico\""' + r)
    f.write(r)
    f.write('[HKEY_CLASSES_ROOT\*\shell\EdShare\command]' + r)
    f.write(r'@="py ' + folder.replace("\\", "\\\\") + r'\\main.py \"%1\""')

    f.close


    # Create uninstall file
    print("Ecriture du fichier de désintallation au registre...")
    f = open('uninstall.reg', 'a')

    f.write('Windows Registry Editor Version 5.00' + r)
    f.write(r)
    f.write('[-HKEY_CLASSES_ROOT\*\shell\EdShare]' + r)
    f.write(r'"Icon"="\"' + folder.replace("\\", "\\\\") + r'\\icon.ico\""' + r)
    f.write(r)
    f.write('[-HKEY_CLASSES_ROOT\*\shell\EdShare\command]' + r)
    f.write(r'@="py ' + folder.replace("\\", "\\\\") + r'\\main.py \"%1\""')

    f.close

    print("Installation terminé")
    print("Lancer uninstall.reg pour désintallé le programme")

else:
    print("Installation annulée")