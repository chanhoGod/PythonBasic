# list comprehension

# country_list = ["USA", "South Korea", "Japan"]

# lower_case_list = []
# for country in country_list:
#     lower_case_list.append(country.lower())

# print(lower_case_list)

# # convert into list conprehension
# new_lower_case_list = [country.lower() for country in country_list]

# print(new_lower_case_list)

# # string list comprehension
# sample = "silicon valley"
# chList = [ch.upper() for ch in sample]
# print(chList)

# conditional list comprehension   원하는 결과 for 밸류값 in 리스트 if 조건문
sampling = [2, 3, 1, 1, 2, 3, 4]
filtered_sampling = [sample * 2 for sample in sampling if sample > 1]
print(filtered_sampling)