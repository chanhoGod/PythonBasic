# # Assignement Operator(=)
# # Assignment with an = on lists does not make a copy. Instead, assignment makes the two variables point to the one list in memory.

# colors = ['red', 'blue', 'green']
# b = colors
# b.append('white')
# print(b)
# print(colors)
## =으로 값을 대입해 주게 되면 같은 주소를 가지고 있기 때문에 복사된 개체에 데이터를 넣어도 원본도 똑같이 값이 추가됨


# Shallow Copy
# A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
# a = [[1, 2], [2, 4]]
# b = a[:] ## shallow copy
# b.append([3, 6])
# print(b)
# print(a)

# b[0].append(3)
# print(b)
# print(a)

# # Deep Copy
# # A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

a = [[1, 2], [2, 4]]
import copy
b = copy.deepcopy(a) ## deep copy
b[0].append(4)
print(b)
print(a)

# # simple list
# a = [1, 2, 3, 4]
# b = a[:]
# b.append(5)
# print(a)
# print(b)