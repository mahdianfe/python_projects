# ماروپله:
#   یه جدول ۱۰۰ خونه در نظر بگیرید
# و داخل اون به صورت رندوم سه مار و چهار نردبان در نظر گرفته بشه
# خونه هایی چیزی داخل آن نیست عدد صفر
# و جایی که مار هست به تعداد خونه هایی که مهره باید به سمت عقب بگردد عدد منفی
# و برای خونه هایی نردبان داخلش هست عدد مثبت در نظر بگیرید
#  بازی تک نفره

# و به همون تعداد بازیکن به سمت جلو برود و همانند مار و پله اگر به نردبان برخورد کرد به سمت جلو به تعداد عدد مثبت داخل خانه جدول و اگر به مار برخورد کرد به سمت عقب برگردد
# اگر به خانه ۱۰۰ رسید برنده است



import numpy as np

jadval = np.zeros(100, dtype=int)

# رندوم مکان مار یا نردبان
index1D_Random_mahal_maar = np.random.choice(np.arange(4, 99), 3, replace=False)
# مقدار 99 را در بازه گذاشتیم چون خانه 100 را که دیگه مار نباید نیش بزنه
index1D_Random_mahal_nardebaan = np.random.choice(97, 4, replace=False)
print(f"mahal maar: {index1D_Random_mahal_maar}")
print(f"mahale nardebaan: {index1D_Random_mahal_nardebaan}")

# رندوم طول مار و نردبان
random_tool_maar = np.random.randint(4, 12, size=3)
random_tool_nardebaan = np.random.randint(3, 10, size=4)

# اصلاح مقادیر در طول مارها (اطمینان از اینکه مقدار نهایی از صفر کمتر نشود)
for i in range(len(random_tool_maar)):
    while index1D_Random_mahal_maar[i] - random_tool_maar[i] < 0:
        random_tool_maar[i] = np.random.randint(4, 12)

# اصلاح مقادیر در طول نردبان‌ها (اطمینان از اینکه مقدار نهایی از 100 بیشتر نشود)
for i in range(len(random_tool_nardebaan)):
    while index1D_Random_mahal_nardebaan[i] + random_tool_nardebaan[i] > 100:
        random_tool_nardebaan[i] = np.random.randint(3, 10)

# اعمال تغییر اصلاحات روی جدول
for i in range(len(index1D_Random_mahal_maar)):
    if index1D_Random_mahal_maar[i] - random_tool_maar[i] >= 0:
        jadval[index1D_Random_mahal_maar[i]] -= random_tool_maar[i]

for i in range(len(index1D_Random_mahal_nardebaan)):
    if index1D_Random_mahal_nardebaan[i] + random_tool_nardebaan[i] <= 99:
        jadval[index1D_Random_mahal_nardebaan[i]] += random_tool_nardebaan[i]

print(jadval.reshape(10, 10))

# ملزومات قبل شروع بازی
index_location = 0

# شروع بازی
while True:
    print("\n________________________")

    # ادامه یا پایان بازی
    taaso_bendazam = input("Taaso Mindazid? Y / N: ").upper()

    if taaso_bendazam == "N":
        print("U az baazi enseraaf daadid!")
        break

    # پرتاب تاس
    taas = np.random.randint(1, 7)
    print(f"Adade Taase U: {taas}")

    # بررسی وضعیت ادامه یا پایان
    if index_location + taas == 100:
        print("U arrived home")
        break

    elif (index_location + taas) > 100:
        index_location = index_location
        # continue

    elif (index_location + taas) < 100:
        index_location += taas

    # قوانین حرکت بازیکن در زمان مار یا نردبان
    if jadval[index_location] > 0:
        print(f"WOW! U {abs(jadval[index_location])} khaane az nardebaan baalaa raftid")
        index_location += jadval[index_location]

    elif jadval[index_location] < 0:
        print(f"Oops! Maar U raa {abs(jadval[index_location])} khaane nish zad")
        index_location += jadval[index_location]

    print(f"U dar khaane {abs(index_location)} gharar darid")