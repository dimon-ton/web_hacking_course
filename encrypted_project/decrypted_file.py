from cryptography.fernet import Fernet

f = Fernet(b'N_SXIQFNZK0poAnCTj5sgoZ0jJJO7DpIi0oZ3GGmSIY=') # insert key value for unique identity

with open('./encrypted_file/encrypted_testing.chang', 'r') as file:

    encrypted_text = file.read()

# convert text to byte because the Fernet read only byte file
byte_code = encrypted_text.encode('utf-8')

decrypted_byte = f.decrypt(byte_code) # decrypt the encrypted byte code file to real content

with open('./decrypted_file/content.pdf', 'wb') as file:

    file.write(decrypted_byte)


