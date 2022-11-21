#2022-11-21 A

import requests

req = requests.get("http://192.168.6.142/readings")
data = req.json()
readings = data["readings"][0]
print(len(readings))