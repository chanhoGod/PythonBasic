#file management
file = open("README.txt", "r")
print(file.read())
file.close()

# memory managment
# # early days
# 1. Forgetting to free your memory 언어 자체에서 메모리를 할당 해제를 시켜줌
# 2. Freeing your memory too soon
# modern language
# - GC Garbage Collector

# # no close any more   r : 읽기, w : 쓰기(overwrite), a : 쓰기(append)
with open("README.txt", "r") as file:
    print(file.read())

with open("WRITEME.txt", "a") as file:
    print(file.write("Thanks"))