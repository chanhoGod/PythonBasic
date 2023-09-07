#Loops - for
alphabets = ["a", "b", "c", "d"];

for alphabet in alphabets:
    print(alphabet);
    print(f"{alphabet} is char")
    

for char in "South Korea":
    print(char)
    
    

numbers = [1,7,2,3,4]
max_num = 0
for number in numbers:
    if number > max_num:
        max_num = number
    
print(max_num)

print(max(numbers))
print(max(1,6,8))


sum2 = 0
for i in range(1, 11, 2):
    sum2 += i;

print("sum2 :",sum2)


sumodd = 0
for i in range(1, 11):
    if i % 2 == 1:
        sumodd += i
        
print(sumodd)