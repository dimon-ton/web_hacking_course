import os
import random
import time
import shutil


path = r'C:\Users\saich\Desktop\trojan-test'

folder_list = os.listdir(path)

result_folder = []
result_file = []


for fd in (folder_list):


    check = fd.split('.')

    if len(check) > 1:
        print('File: ', fd)
        result_file.append(fd)
    else:
        print('Folder: ', fd)
        result_folder.append(fd)


print('folder list: ' , result_folder)
print('file list: ' , result_file)



file_dict = {}

for file in result_file:
    
    select = random.choice(result_folder)
    folderPath = os.path.join(path, select)
    filePath = os.path.join(folderPath, file)

    current = os.path.join(path, file)
    print(current, '------------>', filePath)

    file_dict[file] = {'current': current, 'next': filePath}

while True:
    for k, v in file_dict.items():
        current = v['current']
        nextpath = v['next']
        shutil.move(current, nextpath)



        select = random.choice(result_folder)
        folderPath = os.path.join(path, select)
        file_next = os.path.join(folderPath, k)

        file_dict[k]['current'] = nextpath
        file_dict[k]['next'] = file_next

    time.sleep(2)
