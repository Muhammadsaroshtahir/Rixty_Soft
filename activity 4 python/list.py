cars=["a","b","c"]
print(cars)
print(len(cars))
print(type(cars))

cars1=list(("a","b","c"))
print(cars1)

print(cars[0])
print(cars[1])
print(cars[-1])

cars[0]="Lamborghini"
cars[1]="Audi"
cars[2]="Rolls Royce"
print(cars)

#cars[0:1:2]=["Lamborghini","Audi","Rolls Royce"]
#print(cars)
cars.insert(3,"Farrari")
print(cars)
cars.append("Toyota")
print(cars)

cars2=["honda","Nissan","Mazda"]
cars.extend(cars2)
print(cars)

num=[1,2,3,4,5,6,7,8,9,10]
for x in num:
    print(x)
for x in range(len(num)):
    print(x)
i=0
while i<len(cars):
    print(cars[i])
    i=i+1

#list Comprehension
mycars=[]

for x in cars:
    if "o" in x:
        mycars.append(x)
print(mycars)

cars=[x.upper() for x in cars]
print(cars)

mycars=['buggati' for x in mycars]
print(mycars)

mycars=[x if x != "buggati" else "lamborghini" for x in mycars]
print(mycars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

counting=[1,5,32,57,67,23,22,55,11,88]
counting.sort()
print(counting)

def myfunc(n):
    return abs(n-30)

counting.sort(key = myfunc)
print(counting)

wantcars=[cars]
print(wantcars)

cars=["a","b","c"]

