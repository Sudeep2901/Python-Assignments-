#dump and dumps
import json 
#r = json.dumps({"Key1": 1,"Key2": 2,"Key3": 3,"Key4": 4})
r = '{"Key1": 1,"Key2": 2,"Key3": 3,"Key4": 4}'
with open ("assignment_26.json","w") as f:
    f.write(r)
f.close()

with open ("assignment_26.json","r") as f:
    res = json.load(f)
print(res)
print(type(res))
f.close()