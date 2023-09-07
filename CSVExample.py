# using file
# file = open("country.csv", "r")
# print(file.read())
# file.close()

# # using csv package
# import csv

# with open("sample.csv", "r") as data_file:
#     sample_data = csv.reader(data_file)
#     for row in sample_data:
#         if row[0] != "country":
#             print(row[0])

# using pandas
import pandas as pd

data = pd.read_csv("country.csv")
print(data, '\n')

print(data['country'])