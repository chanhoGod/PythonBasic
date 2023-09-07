#List 
#언제 사용하는지?
#Grouping
#Keep the order

countries = ["korea", "USA", "China"];

print(countries);

countries[2] = "vietnam";

print(countries);


element = "c"
alphabets = ["b", element, "d"];
print(alphabets);

alphabets.append("e");
print(alphabets);

alphabets += ["f", "g"];
print(alphabets);

alphabets.insert(0, "a");
print(alphabets);

print(countries[0]);
print(countries[len(countries) - 1]);
print(countries[-1]);


print(countries.pop());
print(countries);

print(countries.pop(0));
print(countries);
