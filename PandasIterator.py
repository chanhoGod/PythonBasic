score_dict = {
    "student": ["Tom", "Lisa", "Sarah"],
    "score": [80, 90, 95]
}

# # # Iterating thru    값을 주고싶지 않을때 _를 줌
# [print(col, row) for (col, row) in score_dict.items()]
# print({student:score for (student,score) in score_dict.items()})

import pandas as pd

score_df = pd.DataFrame(score_dict)
print(score_df)
# for (key, value) in score_df.items():
#     print(key)
#     print(value)

# # loop through rows
# for (i, row) in score_df.iterrows():
#     print(f"{row.student} : {row.score}")