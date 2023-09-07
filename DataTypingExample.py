# Data Types
# int, float, str, bool

# casting, dynamic typing
# int(3.5)

age: int = 0                #변수를 사용할때 처음 데이터 타입을 할당해줄 수 있음
name: str = "Hello"
height: float = 6.0
is_student: bool = True
print(name)


def enter_school(is_student: bool) -> bool:
    if is_student:
        return True
    else:
        return False


# # How to check the type of parameter?
enter_school()

# # Type Hints