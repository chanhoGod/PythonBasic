# reverse String
value = "hello world"

#1. reverse
value_list = list(value)
value_list.reverse()
print("".join(value_list))


#2. reversed
print("".join(list(reversed(value))))


#forloop
tmp_list = []
for i in range(len(value)-1, -1, -1):
    tmp_list.append(value[i])

print("".join(tmp_list))


while_value_list = list(value)
tmp_list2 = []
while len(while_value_list) > 0:
    tmp_list2.append(while_value_list.pop())

print("".join(tmp_list2))