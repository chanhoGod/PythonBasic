# Custom Class
# naming convention
# PascalCase : class name
# camelCases : object name
# snake_case : anything else
from TMPCar import Car as c #클래스 이름이 길때 alias를 지어줄 수 있음

tesla = c(color='red', engine_type='electric')


# tesla.color = 'red'
# tesla.engine_type = 'electric'

print(tesla.color)


# 어떤 attribute를 가지고 있는지 확인하는 코드
print(vars(tesla))

tesla.start_engine()
print(vars(tesla))

for i in range(1, 5):
    tesla.speed_up(1)
    print(tesla.speed)

for i in range(1, 5):
    tesla.speed_down(1)
    print(tesla.speed)


# constructor 클래스가 생성될때 자동으로 실행되는 메서드
# def __init__(self):
#     pass