print("***The process is that you choose two numbers.\n"
      "Then you can guess 5 times which number the robot choose from among these two numbers?\n"
      "Don't worry, the robot will help you!***")
a=input("what is your first number? ")
a=int(a)
if  type(a) != int:
    print("It's not a number!")
    a=input("plz enter a number as first number?")

b=input("what is your second number? ")
b=int(b)
if  type(b) != int:
    print("It's not a number!")
    b=input("plz enter a number as second number?")
import random
c=random.randint(int(a),int(b))
# print(c)
d=input("guess which number the robot choose from among these two numbers: ")
d=int(d)
if  type(d) != int:
    print("It's not number!")
    d=input("plz enter a number?")
i=0
while i<4:
    if c==int(d):
        print("It's correct. YOU WON!")
        break
    elif c < int(d):
        print("It's wrong!choose a smaller number!")
        d=input("What number do you think it could be?")
    elif c > int(d):
        print("It's wrong!choose a biger number!")
        d=input("What number do you think it could be?")
    i = i + 1
if i == 5:
    print("YOU LOST")
print(__name__)