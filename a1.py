import requests as r
import json


url = 'https://api.github.com/users/FallSpir/repos'
response = r.get(url)
response_json = response.json

for repo in response_json:
    print(f'Repo:{repo["name"]}, URL:{repo["html_url"]}')
