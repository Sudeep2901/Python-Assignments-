#Data Type : List

#syntax for list
_list = ["one","two","three","four",5,6,7]
print(f"simple list : {_list}")

#elements : accessing through index in simple list
print(_list[0:1])   #get item as a list
print(_list[0])     #gives actual value

#syntax for multidimensional list
list_1 = [[1,2,3],[4,5,6]]
print(f"Multidimensional list : {list_1}")

#elements : accessing through index in multidimensional list
print(f"at index 0,1 : {list_1[0][1]}")     #2-D indexing
print(f"at index 1,1 : {list_1[1][1]}")

#reassignment : reassigning/replacing of values at index
_list[3] = 4
print(f"Reassignment at index 3 : {_list}")

#append : add at the end
_list.append(8)     #takes only one parameter
print(f"Append in a list : {_list}")

#insert : to insert item in a list
_list.insert(8,"9")     #takes two parameters = index and value
print(f"Iserted with item : ",_list) 

#clear : deleting all elements in a list
list_1.clear()
print(f"cleared multidimensional list : {list_1}")

#copy : copying old list items into new list
list_2 = []
list_2 = _list.copy()
print(f"copies from _list : {list_1} into list 2 : {list_2}")

#count : count occurence of a item in a list
i = _list.count("one")
print(f"count of element one : {i}")

#extend : insert multiple items at the end of list
addon_List = [10,11,12]
_list.extend(addon_List)
print(f"extended list : {_list}")

#pop : to remove last element from list 
_list.pop()     #removes last by default
_list.pop(7)    #takes only one argument that is index
print(f"list with used pop at end and at index 7 : {_list}")

#remove : removes element from list
_list.remove(5)     #takes actual value
print(f"removed elemrnt at index 5 : {_list}")

#sort: sorting is by default ascending 1 upto n or in alphabetical order A to Z
cities_in_maharashtra = ["Mumbai", "Pune", "Nagpur"]
print(cities_in_maharashtra)
cities_in_maharashtra.sort()
print(cities_in_maharashtra)

#sorting in descending
cities_in_maharashtra = ["Mumbai", "Pune", "Nagpur"]
print(cities_in_maharashtra)
cities_in_maharashtra.sort(reverse=True)    #reverse paramter =true 
print(cities_in_maharashtra)

#Sort By Length of string/element
def sortBylength(e):
    return len(e)
cities_in_maharashtra = ["Mumbai", "Pune", "Nagpur","Wai"]
print(cities_in_maharashtra)
cities_in_maharashtra.sort(key=sortBylength)        #key parameter
print(cities_in_maharashtra)

#sort by descending and length
cities_in_maharashtra = ["Mumbai", "Pune", "Nagpur","Wai"]
print(cities_in_maharashtra)
cities_in_maharashtra.sort(reverse=True, key=sortBylength)
print(cities_in_maharashtra)