import json

ls=[[1],[2]]
print (ls)

x = {
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
# with open("json.txt",'w') as outfile:
#   json.dump(x,outfile)

z=open("json.txt",'w')
json.dump(x,z)
z=open("json.txt",'r')
y=json.load(z)
b=y['cars']
a=b[0]
print(a['mpg'])