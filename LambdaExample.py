# lambda expressions

# It his small anonymous function

# lambda arguements : expression                    #람다는 간단한 함수를 만들 수 있는 기능

# def square(num):
#     return num**2

# print(square(3))

# square = lambda num: num**2
# print(square(3))

number_list = [1, 2, 3, 4, 5]
print(list(map(lambda num: num**2, number_list)))
print(list(filter(lambda num: num % 2 == 0, number_list)))

