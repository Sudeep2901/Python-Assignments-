#Inserting in a complex list
list_1 = [1,2,3,[4,5,6]]
existing_list = []

for i in list_1:
    _index = list_1.index(i)
    if(type(list_1[_index])==list):
        print(f"List found at Index : {_index}")
        _elist = list_1[_index]
        print(_elist)
        _elist.insert(3,7)
        print(_elist)

list_1.pop()
list_1.append(_elist)
print(list_1)