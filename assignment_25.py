# load & loads is used to fetch data
import json
import os
d = '{"Key1": 1,"Key2": 2,"Key3": 3,"Key4": 4}'
f = json.loads(d)
print(f)
print(type(f))

j = open("assignment_25.json","r")
k = json.load(j)
print(k)
print(type(k))