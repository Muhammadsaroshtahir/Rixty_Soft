import modules as m
m.greeting("jonathan")

a=m.person1["age"]
print(a)

import platform as pf
x=pf.system()
print(x)

x=dir(pf)
print(x)

import datetime

x=datetime.datetime.now()
print(x)

y=datetime.datetime.now()

print(y.year)
print(y.strftime("%A"))
print(y.strftime("%B"))
print(y.strftime("%Y"))

z=datetime.datetime(2020,5,17)
print(z)

import math

a=math.ceil(2.12)
b=math.floor(2.12)
c=math.pi
d=math.sqrt(128)

print(a)
print(b)
print(c)
print(d)