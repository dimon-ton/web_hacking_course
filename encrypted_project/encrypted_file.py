'''
Example from uncle engineer github

https://github.com/UncleEngineer/Trojan-Python.git


'''

from cryptography.fernet import Fernet

key = Fernet.generate_key()

print('key generated: ', key)

f = Fernet(key)


# open file and get binary of file
file_path = './encrypted_file/doc.pdf'
with open(file_path, 'rb') as file:
    docFile = file.read()


encrypted_byte = f.encrypt(docFile) # encrypt file that has read out

# write encrypted code to a file
with open('./encrypted_file/encrypted_testing.chang', 'w') as file:
    
    # change byte type to str type because byte file cannot be to written.
    strMsg = encrypted_byte.decode('utf-8')
    file.write(strMsg)





