import json
x={
    "name":"Sarosh",
    "age":"30",
    "city":"new york"
}
y=json.dumps(x)
print(y)

z = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(z, indent=4, sort_keys=True))
