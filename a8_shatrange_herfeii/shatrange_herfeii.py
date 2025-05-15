
# https://quera.org/problemset/2636

listt = (input())
listt = listt.split()

# برای شاه و وزیر
for i in range(2):
    if int(listt[i]) < 1:
      listt[i]=1

    elif int(listt[i]) == 1:
        listt[i]=0

    elif int(listt[i]) > 1:
      listt[i] =-(int(listt[i]) -1)

# برای تعداد دوتا
for i in range(2,5):
    if int(listt[i]) == 0:
      listt[i]=2-int(listt[i])

    elif int(listt[i]) == 2:
        listt[i]=0

    elif int(listt[i]) > 2:
      listt[i] =-(int(listt[i]) -2)

# برای سرباز
if int(listt[5]) < 8:
  listt[5] = 8 - int(listt[5])

elif int(listt[5]) == 8:
    listt[5]=0

elif int(listt[5]) > 8:
  listt[5] =-(int(listt[5]) - 8)

print(f"{listt[0]} {listt[1]} {listt[2]} {listt[3]} {listt[4]} {listt[5]}")