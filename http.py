import requests

req = requests.request('GET', 'http://api.github.com/users/dennomwas')
print(req.json()) 


