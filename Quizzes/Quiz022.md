# Quiz 022

## Prompt
Create a program that produces n random values from the equation below , where m and s are the other inputs of the function

#### $y = x^{1/2*(m/s)^2}$

HL: Show A(A+B)=A

## Code Structure 
```.py
#2022-11-08 Quiz 022

#Prompt : Create a program that produces n random values from the equation below , where m and s are the other inputs of the function

#y = x**(1/2*(m/s)**2)

#n = number of random values to produce

import random

random.seed(1234)

def produce(n,m,s):
    print(f"|    x     |   y(x)   |")
    for i in range(n):
        x = random.randint(0,100)
        y = round(x**(1/2*(m/s)**2),2)
        x =str(x).center(10)
        y =str(y).center(10)
        print(f"|{x}|{y}|")
    return ""
print(produce(n=5,m=3,s=2))
```

## Evidence
![](/Assets/Quiz022_Evidence.jpg)
*Fig.1* **Screenshot showing the result of the program**

## HL Part
![](/Assets/Quiz022_Boolean.jpg)

*Fig.2* **Proof that _A(A+B)=A_**

