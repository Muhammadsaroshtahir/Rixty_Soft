thisdict = {
    "brand": "Ford" ,
    "model": "Selby",
    "year" : 2022
}
print (thisdict)
print (thisdict["model"])
print (thisdict["year"])
print (len(thisdict))
print (type(thisdict))

x=thisdict.get("brand")
print(x)
y=thisdict.keys()
print(y)
z= thisdict.values()
print(z)

thisdict.update({"year":2023})
print(thisdict)