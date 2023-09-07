import time
from turtle import Turtle

john = Turtle()
print(john)

john.shape("turtle")
john.color("red", "green")

while True:
    john.forward(5)
    john.left(5)
    time.sleep(0.1)