import requests
import json

name_team = "NISA"
url = 'https://buuoj.cn/api/v1/scoreboard/top/All/10?affiliation=' + name_team
headers = {
    "Host": "buuoj.cn",
    "Cookie": "lang=zh;UM_distinctid=17be989b3b9b0a-0d379f20321823-c343365-144000-17be989b3baab5; CNZZDATA1279426740=314227466-1631707613-%7C1631707613; session=e3fbf1d9-6c5f-408f-8ac9-d4c1a28cb03c.DBAUE3zeD28wmqJiO3EPksB0KCI",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
}

s_output = []
print(url)
response_ = requests.get(url, headers=headers)
print(response_.text)
data = json.loads(response_.text)["data"]
# print(data)
