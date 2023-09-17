from tkinter import *
from tkinter import ttk
import ftplib
import os
import subprocess

# Github url for study GUI Hacking
# https://github.com/UncleEngineer/GUI-CIA
# https://github.com/UncleEngineer/DieHard4UI

# set ip, username and password

ip = '-------------' # insert ip address
port = 21
username = '-------------' # insert username
password = '--------------' # insert password

def download():
  

    ftp = ftplib.FTP() # annouce FTP object
    ftp.connect(ip, port)
    ftp.login(username, password)


    local_path = os.getcwd()
    mypath = '/home/dimon/Documents/' # insert path from server
    ftp.cwd(mypath) # change working directory

    # with open('uploadfile-local.txt', 'wb') as fp:
    #     ftp.retrbinary('RETR uploadfile.txt', fp.write)

    files = ftp.nlst()
    print(files)

    ftp.close()

    # set file in folder
    text = ''

    # clear data in table
    fileList.delete(*fileList.get_children())

    ignore_list = ['..','.']
    for f in files:
        if f not in ignore_list:
            text = text + f + '\n'
            fileList.insert('', 'end', value=[f])

    # v_result.set(text)
    





GUI = Tk()
GUI.title('Hacking Command Center')
GUI.geometry('800x600+50+50')

F1 = Frame(GUI)
F1.place(x=610, y=50)

v_result = StringVar()
v_result.set('')

L = Label(GUI, textvariable=v_result, font=('Angsana New', 20), justify=LEFT)
L.place(x=50, y=50)

B1 = Button(F1, text='Check Folder', command=download)
B1.pack(ipadx=20, ipady=20)



###### TREE VIEW ########
header = ['File/Folder']
fileList = ttk.Treeview(GUI, height=20, columns=header, show='headings')
fileList.place(x=50, y=50)

fileList.heading('File/Folder', text='File/Folder')
# resize column
fileList.column('File/Folder', width=300)

# fileList.insert('', 'end', value=['1'])
# fileList.insert('', 'end', value=['2'])
# fileList.insert('', 'end', value=['3'])
# fileList.insert('', 'end', value=['4'])
# fileList.insert('', 'end', value=['5'])



def downloadFile():

    # get file name and take to stp server

    select = fileList.selection()
    data =  fileList.item(select)
    # print(data['values'][0])

    fileName = data['values'][0]



    # STP server section

    ftp = ftplib.FTP() # annouce FTP object
    ftp.connect(ip, port)
    ftp.login(username, password)


    local_path = os.getcwd()
    mypath = '/home/dimon/Documents/' # insert path from server
    ftp.cwd(mypath) # change working directory

    with open(fileName, 'wb') as fp:
        ftp.retrbinary('RETR {}'.format(fileName), fp.write)

    # open file ---> we have to use "subprocess"
    subprocess.Popen(fileName, shell=True)

    ftp.close()

    

B2 = Button(F1, text='Dowload', command=downloadFile)
B2.pack(pady=12, ipadx=20, ipady=20)

GUI.mainloop()