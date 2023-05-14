from requests import get # pip install requests

info = 'https://api.open-meteo.com/v1/forecast?latitude=-31.37&longitude=-51.98&timezone=auto&current_weather=true'

get = get(info)

print(get.status_code)

dados = get.json()

get.close()

print(dados)

for k, v in dados.items():
  print(k, v)