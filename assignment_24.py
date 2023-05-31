# Generator
def Rainbow():
    yield "Violet"
    yield "Indigo"
    yield "Blue"
    yield "Green"
    yield "Yellow"
    yield "Orange"
    yield "Red"


# Direct Method
count = 0
for i in Rainbow():
    count += 1
    print(count, i)
print("------------")
# Manual Method
n = Rainbow()
print("1", next(n))
print("2", next(n))
print("3", next(n))
print("4", next(n))
print("5", next(n))
print("6", next(n))
print("7", next(n))

# *******************************
# Iterator

New_List = [2, 4, 6, 8, 10]

# Direct Method
for i in New_List:
    print(i)

# Manual Method
Even_Iterator = iter(New_List)
print(next(Even_Iterator))
print(next(Even_Iterator))
print(next(Even_Iterator))
print(next(Even_Iterator))
print(next(Even_Iterator))
