# Created By: RITIK AGARWAL

import os
import webbrowser

print('\n         --- Upgradable Commands Follower Program ---\n\n')
a = {
    'open notepad' : 'notepad',
    'uninstall program' : 'control appwiz.cpl',
    'open file explorer' : 'explorer'
}

b = {
    'open youtube' : 'www.youtube.com',
    'open github' : 'www.github.com',
    'open whatsapp' : 'www.web.whatsapp.com',
    'open google' : 'www.google.com',
    'open amazon' : 'www.amazon.in'
}

while (True):
    x = 0; y = 0
    print('-- To know commands input "cmds" else press ENTER --')
    hlp = input('>>> ').lower()
    
    if hlp == 'cmds':
        c = 1
        for i in a:
            print('  ' + str(c) + '.) ' + i)
            c += 1
    
        for j in b:
            print('  ' + str(c) + '.) ' + j)
            c += 1

    c = input('\n> Enter command: ').lower()

    for elem1 in a:
        if elem1 == c:
            os.system(a[elem1])
            x = 1
    for elem2 in b:
        if elem2 == c:
            webbrowser.open(b[elem2])
            y = 1
    
    if x == 0 and y == 0:
        print('\n>>> Command not found! <<<\n')
        f = input('> Do you want to save this command (Y/N): ').lower()
        
        while f == 'y':
            fw = input('\n> Its a file or website:-\n- File(f)\n- Website(w)\n> ')
            if fw == 'f' or fw == 'w':
                break
            else:
                print('\n>>> Invalid Choice! <<<\n')
        
        if f == 'y' and fw == 'f':
            while True:
                path = input('\n> Enter the file path: ')
                if os.path.exists(path):
                    a[c] = path
                    print('\n > SAVED SUCCESSFULLY <')
                    break
                else:
                    print('\n>>> Invalid path <<<\n')
                    ch = input('\n> Do you want to input again ?(Y/N): ').lower()
                    if ch == 'n':
                        break
                    elif ch == 'y':
                        continue
                    else:
                        print('\n>>> Invalid Input <<<\n')
        
        elif f == 'y' and fw == 'w':
            web = input('\n> Enter website: www.')
            b[c] = 'www.' + web
            print('\n > SAVED SUCCESSFULLY <')
    
    print('\n-----------------------------------------------------\n')