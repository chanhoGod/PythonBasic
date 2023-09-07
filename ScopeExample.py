# scope
# local scope / global scope / enclosed scope / enclosing scope
# namespace

my_score = 50

# def inside_value_function():
#     global my_score #global키워드가 있다면 밖에있는 변수명을 가지고 오게 됨
#     my_score = 80  #global키워드가 없다면 신규로 할당하게 됨 
#     print(f"my score inside is {my_score}")


# inside_value_function()
# print(f"my score outside is {my_score}")

# What about if condition
# did_extra_work = True
# if did_extra_work:          #if나 for의 경우에는 새로운 namespace를 생성하지 않는다.
#     my_score = 90

# print(f"my score outside is {my_score}")

# nonlocal 
def a():
    x = 10
    def b():
        nonlocal x
        x = 20
    b()
    print(x)

a()


# How Python search the variable?
# (LEGB rule)
# 1. local
# 2. enclosing
# 3. global
# 4. built-in

# # builtin namespace
# print(dir(__builtins__))

# # # However ...
# country = ["south korea"]

# def inside_list_function():
#     # country.append("usa")
#     country = ["usa"]

# inside_list_function()
# print(country)


# # globals keyword
# print(globals())

# Global Constant?
# HTTP_ENDPOINT = "https://google.com"

# def print_us_restaurant_url():
#     print(f"{HTTP_ENDPOINT}/biz/arya-steakhouse-palo-alto")

# def print_korean_restaurant_url():
#     print(f"{HTTP_ENDPOINT}/biz/tobang-santa-clara-2")
