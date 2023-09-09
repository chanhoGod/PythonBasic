# map function

def square(num):
    return num**2

print(square(3))

number_list = [1, 2, 3, 4, 5]

print(map(square, number_list)) #Map은 function과 list를 인자로 가져가게 됨 list의 하나하나를 function에 처리

# for i in map(square, number_list):
#     print(i)

# # or

# print(list(map(square, number_list)))

# # How about multiple arguments?
def sum(a, b):
    return a + b

lst1 = [2, 4, 6, 8]                     #리스트가 하나 없게된다면 있는 짝만을 찾아 계산함
lst2 = [1, 3, 5, 7, 9]
print(list(map(sum, lst1, lst2)))

# filter function                       #filter function은 True일때만 반호나 가능
def is_even(num):
    return num % 2 == 0
# print(is_even(3))
number_list = [1, 2, 3, 4, 5]
print(list(filter(is_even, number_list)))