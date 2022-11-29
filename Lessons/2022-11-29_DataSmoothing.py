#2022-11-29

import requests
import numpy as np
from matplotlib import pyplot as plt

req = requests.get("http://192.168.6.142/readings")
data = req.json()
readings = data["readings"][0]
print(len(readings))

temp = []
for sample in readings:
    if sample["sensor_id"] == 1:
        temp.append(sample["value"])
print(len(temp))

#Every 12 samples calculate the mean and std
number_samples_per_hour = 12
mean_per_hour = []
std_per_hour = []
x = []
for i in range(0, len(temp), number_samples_per_hour):
    mean_per_hour.append(np.mean(temp[i:i+number_samples_per_hour]))
    std_per_hour.append(np.std(temp[i:i+number_samples_per_hour]))
    x.append(i)

fig=plt.figure(figsize=(9,6))
plt.subplot(2,1,1)
plt.plot(temp)
plt.subplot(2,1,2)
plt.plot(x,mean_per_hour)
plt.show()
