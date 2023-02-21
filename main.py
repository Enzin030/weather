import requests
import json

APIKEY="87a64548c577e19348426892c5b7e959"
url = 'https://api.openweathermap.org/data/2.5/weather?q=Taichung&units=metric&appid='+APIKEY
r = requests.get(url)
data = json.loads(r.text)

temp = data['main']['temp']
feels_like =data['main']['feels_like']
temp_max=data['main']['temp_max']
temp_min=data['main']['temp_min']

msg = f"早安 \n當前氣溫 {temp} \n體感溫度 {feels_like}\n最高溫 {temp_max}\n最低溫 {temp_min}"
url = "https://notify-api.line.me/api/notify"
payload={'message':{msg}}
headers = {'Authorization': 'Bearer ' + 'hT77z3cY1siodkVoehRDsU5HNZph5uEnK2d56VTBiGF'}
response = requests.request("POST", url, headers=headers, data=payload)