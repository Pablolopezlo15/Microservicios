#https://www.el-tiempo.net/api/json/v2/provincias/04/municipios/04088

import requests
import json

url = "https://www.el-tiempo.net/api/json/v2/provincias/04/municipios/04088"
response = requests.get(url)
data = response.json()

print(data.get("municipio").get("NOMBRE_CAPITAL"))
print(data.get("temperatura_actual"))