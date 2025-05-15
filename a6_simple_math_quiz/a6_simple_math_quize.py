# امتحان از جمع و ضرب و تفریق اعداد 1 تا 9
#  وقت دارید تا کمتر از 4 ثانیه حدس بزنید

import time
import random
operation=["+","-","*"]
i=1
while i<4:
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    n3 = random.choice(operation)
    if n3 == "+":
        result = n1 + n2
    if n3 == "-":
        result = n1 - n2
    if n3 == "*":
        result = n1 * n2

    start=time.time()
    print("4 Question in less than 4S")
    answer=input(f"Please answer question number {i} in less than 4 seconds => {n1}{n3}{n2}=")
    answer=int(answer) #باید همیشه خروجی تبدیل به اینتیجر شود چون همیشه استرینگ دریافت میشود
    End=time.time()

    if End-start>=4 or answer!=result:
        print("YOU LOST TIME!")
        break
    if End-start<4 and answer==result:
        print("That's right")
    if  i==3 :
        print("YOU WON!")

    i=i+1
