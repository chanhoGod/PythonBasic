# spcial, magic, dunder __xxx__


class Tesla(object):

    def __init__(self, owner, color):               #생성자
        self.owner = owner
        self.color = color

    def __str__(self):
        return f"This is {self.color} color {self.owner}'s car"  #Object 프린트시 출력될 내용 tostring같은 역할

    def __len__(self):                              #Object를 Len처리했을때 출력할 내용
        return len(self.owner)

    def __del__(self):                              #del function을 사용해서 개체를 삭제했을때 출력되는 메시지
        print("This car has been deleted")

    def __eq__(self, other):                        #개체끼리 비교를 할때 사용하는 function
        return self.color == other.color


tesla = Tesla("Joon", "Yellow")
# print(tesla)
# del tesla

tesla1 = Tesla("Aain", "White")
print(tesla == tesla1)

