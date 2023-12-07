from cryptography.fernet import Fernet

f = Fernet(b'Fwhr5dPpPn6lF05gYxIv0eo6Jd91wsLvvGfRcL3NAdE=')

text = "gAAAAABlcH36DJnfNZ_fnPc0s1uo5VSa2k0J7_6isX0nuERVAKAHQp15MIAVJ8LZQVpMkOp14wyg1MefARtXa2S4rUqocASzPMgL2VLpm5RmQzicRjVlPieytw5XnUhmmmGPqTdoI1jComCZNeh54vXVJNRhtgY2VUVeBTBs4lcm1xVSO5p10zs610EdvfYx0bv-at1cUpSR"

text_convert = text.encode('utf-8') # convert string format to byte format

print('text_convert: ', text_convert)

text_decrypt = f.decrypt(text_convert) # decrypt byte format to true data

print('text_decrypt: ', text_decrypt)


print(text_decrypt.decode('utf-8'))
