from cryptography.fernet import Fernet

f = Fernet(b'1kAuwkkdV7qgfvzZ60uJh6MU9B7e-kUDrr98YopQYG0=')

text = "gAAAAABlcHQNwUImgoRSEwxqXUAWNpjqZeZv4uzRyjZDIkruOgJMwzvZL5Jgj9GAzh0K4woU_afL0_zK13PuM780Xp6WRd-sVgoc2uhUiOm5MLeALItm89E2yb_DWqHyrmEP_UzSiX2I4hXvBhTKnJFnKp-jlii4ONnjtY5UovQLe5tSSkor66NZw1sZyXOgt-GmFVEuvXHD"

text_convert = text.encode('utf-8') # convert string format to byte format

print('text_convert: ', text_convert)

text_decrypt = f.decrypt(text_convert) # decrypt byte format to true data

print('text_decrypt: ', text_decrypt)


print(text_decrypt.decode('utf-8'))
