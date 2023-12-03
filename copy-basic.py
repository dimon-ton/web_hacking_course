import os
import os

import time
import shutil


path = r'C:\Users\saich\Desktop\trojan-test'

file = os.path.join(path, 'homeWork.docx')

new_file = 'homework3.docx'

for i in range(4, 10):
    copyfile = os.path.join(path, new_file)
    shutil.copyfile(file, copyfile)

    new_file = 'homework{}.docx'.format(i)

    time.sleep(2)