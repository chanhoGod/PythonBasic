# Grading program
# grading A if >= 90, B if >= 80, C if >= 70 otherwise F

students = {
    "tom": 82,
    "jerry": 93,
    "joon": 99,
    "misha": 80,
    "amy": 74
}

def grading_check(score : int):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'


for name, score in students.items():
    print(f"{name}'s score is {score}")
    print(f"then, {grading_check(score)}")