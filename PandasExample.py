import pandas as pd

data = pd.read_csv("country.csv")

# DataFrame : General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed column == 테이블
# print(type(data))
# print(data.to_dict())

# # Series : 1D labeled homogeneously-typed array == 컬럼
# print(type(data['country']))
# print(data['country'])
# print(data['country'].to_list())

# # sum / max
# print(sum(data['population'].to_list()))
# print(data['population'].max())

# differct way to access to the column
# print(data.population)

# def returnMax(data : pd):
#     return data.population.max()

# # row data 괄호안에 조건을 주어서 원하는 데이터 추출 가능
# print(data[data.country == "USA"])
# print(data[data.population == returnMax(data)])

# from scratch
grade = {
    "students": ["A", "B", "C"],
    "scores": [90, 80, 85]
}
data =pd.DataFrame(grade)
print(data)
data.to_csv("grade.csv")

