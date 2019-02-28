import ctypes
import os
import time

def lock():
    return ctypes.windll.user32.LockWorkStation()

def displayoff():
    return ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)

def displayon():
    return ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)

def editAccessed(editfile, edittime):
    if os.path.exists(editfile):
        cmd ='powershell "Get-ChildItem \'%s\' | %% { $_.LastAccessTime = \'%s\' }"' % (editfile,edittime)
        return os.system(cmd)
    else:
        resp = "[!] {}: No such file or directory\n".format(editfile)

def editCreation(editfile, edittime):
    if os.path.exists(editfile):
        cmd ='powershell "Get-ChildItem \'%s\' | %% { $_.CreationTime = \'%s\' }"' % (editfile,edittime)
        return os.system(cmd)
    else:
        resp = "[!] {}: No such file or directory\n".format(editfile)

def editModified(editfile, edittime):
    if os.path.exists(editfile):
        cmd ='powershell "Get-ChildItem \'%s\' | %% { $_.LastWriteTime = \'%s\' }"' % (editfile,edittime)
        return os.system(cmd)
    else:
        resp = "[!] {}: No such file or directory\n".format(editfile)


def tests():
    displayoff()
    time.sleep(5)
    displayon()
    editAccessed('d:/say.txt', '8/10/11')
