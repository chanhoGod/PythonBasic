# # List  대괄호 []
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
my_list[1] = 0
print(my_list)

# # Dictionary 중괄호 {} 키밸류 값으로 사용가능
# # As of Python3.7, it is ordered 순서 저장이 됨
my_dictionary = {
    "country": "south korea",
    "city": "seoul"
}
print(my_dictionary)
my_dictionary['country'] = "USA"
print(my_dictionary)

# # Set 소괄호 ()
# # it is unchangeable, but can add or remove
# # cannot subscript, unique
# Set은 같은 밸류를 다시 넣을 수 없음 List -> Set으로 변경할때 중복된 값은 사라져버림
# set은 단일 인덱스를 읽기는 불가능 순서가 보장되지 않음
my_set1 = set((1, 2, 3))
print(my_set1[1])
# print(my_set1)
# my_set1.add(1)
# print(my_set1)
# l = [1, 2, 3, 4, 1, 2, 3, 4]
# print(list(set(l)))
my_set2 = {1, 2, 3}
print(my_set2)
my_set2.add(4)
print(my_set2)
my_set2.remove(4)
print(my_set2)


# # Tuples 소괄호 ()
# # Once it is created, you cannot change
# # it is immutable
# # Creation is fater than list  생성시 리스트보다 빠름 다만 한번 생성시 변경 불가
# my_tuples = (1, 2, 3)
# print(my_tuples[1])