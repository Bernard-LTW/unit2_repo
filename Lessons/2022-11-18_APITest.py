#Get JSON API from 192.168.6.142/readings

import requests
import json
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("dark_background")

url = "http://192.168.6.142/readings"

response = requests.get(url)
data = json.loads(response.text)
print(data)