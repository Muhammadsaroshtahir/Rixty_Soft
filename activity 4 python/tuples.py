x = ("apple", "banana", "cherry")
y = list(x)
print(y)
y[1] = "kiwi"
print(y)
x = tuple(y)
print(x)

z=list(x)
z.append("mango")
x=tuple(y)
print(y)


#obe = [(1,2),(2,3)]
#obe[1][0]=5
#print(obe)
#
obe = ([1,2],[2,3])
obe[1][0]=5
print(obe)
