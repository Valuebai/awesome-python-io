import requests

url = ''
data = {
    'username': 'mushishi',
    'password': '111111'
}

res = requests.post(url, data)
print(res.text)
