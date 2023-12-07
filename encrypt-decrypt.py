# learing about cryptography

# pip install cryptography

from cryptography.fernet import Fernet

key = Fernet.generate_key()

print('Fernet Key: ', key)

f = Fernet(key) # Object Fernetg

text = 'สวัสดีจ้า ข้อความจากลุงเองจ้า'

message = f.encrypt(text.encode('utf-8')) # ใช้ภาษาไทย ใช้ utf-8

# print(message)
print('=====================Encrypt==================================')
print(message.decode('utf-8'))
print('==============================================================')