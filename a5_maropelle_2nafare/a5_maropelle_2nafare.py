# ماروپله:
#   یه جدول ۱۰۰ خونه در نظر بگیرید
# و داخل اون به صورت رندوم سه مار و چهار نردبان در نظر گرفته بشه
# خونه هایی چیزی داخل آن نیست عدد صفر
# و جایی که مار هست به تعداد خونه هایی که مهره باید به سمت عقب بگردد عدد منفی
# و برای خونه هایی نردبان داخلش هست عدد مثبت در نظر بگیرید
#  بازی دارای دو بازیکن یک و دو هست
# در نوبت هر بازیکن باید به عنوان تاس از عدد یک تا شش یک عدد رندوم تولید شود
# و به همون تعداد بازیکن به سمت جلو برود و همانند مار و پله اگر به نردبان برخورد کرد به سمت جلو به تعداد عدد مثبت داخل خانه جدول و اگر به مار برخورد کرد به سمت عقب برگردد
# هر بازیکنی که زود تر به خانه ۱۰۰ رسید برنده است




import numpy as np

jadval = np.zeros(100, dtype=int)

# رندوم مکان مار یا نردبان
index1D_Random_mahal_maar = np.random.choice(np.arange(4, 99), 3, replace=False)
index1D_Random_mahal_nardebaan = np.random.choice(97, 4, replace=False)

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

# اعمال تغییر اصلاحات روی جدول برای مارها و نردبان ها
for i in range(len(index1D_Random_mahal_maar)):
    if index1D_Random_mahal_maar[i] - random_tool_maar[i] >= 0:
        jadval[index1D_Random_mahal_maar[i]] -= random_tool_maar[i]

for i in range(len(index1D_Random_mahal_nardebaan)):
    if index1D_Random_mahal_nardebaan[i] + random_tool_nardebaan[i] <= 99:
        jadval[index1D_Random_mahal_nardebaan[i]] += random_tool_nardebaan[i]

print(f"mahal maar: {index1D_Random_mahal_maar}")
print(f"mahale nardebaan: {index1D_Random_mahal_nardebaan}")

# پرینت جدول ماروپله
print(jadval.reshape(10, 10))

# ملزومات تبدیل بازی به دو بازیکن
index_location = {1: 0, 2: 0}  # موقعیت شروع بازیکنان
noobat = 2

# شروع بازی
while True:
    noobat = 1 if noobat == 2 else 2  # مربوط به تغیر نوبت

    print("\n________________________")

    # ادامه یا پایان بازی
    taaso_bendazam = input(f"Bazikone{noobat} Taaso Mindazid? Y / N: ").upper()
    if taaso_bendazam == "N":
        print(f"Bazikone{noobat} az baazi enseraaf daad!")
        break

    # پرتاب تاس
    taas = np.random.randint(1, 7)
    print(f"Adade Taase Bazikone{noobat}: {taas}")

    # بررسی وضعیت ادامه یا پایان
    if index_location[noobat] + taas == 100:
        print(f"Bazikone{noobat} arrived home")
        break

    elif (index_location[noobat] + taas) > 100:
        # index_location_baraye_100shodan= index_location[noobat] -taas
        index_location[noobat] = index_location[noobat]
        # continue

    elif (index_location[noobat] + taas) < 100:
        index_location[noobat] += taas

    # قوانین حرکت بازیکن در خانه مار یا نردبان
    if jadval[index_location[noobat]] > 0:
        print(f"WOW! Bazikone{noobat}, {abs(jadval[index_location[noobat]])} khaane raa az nardebaan baaalaa raftid")
        index_location[noobat] += jadval[index_location[noobat]]

    elif jadval[index_location[noobat]] < 0:
        print(f"Oops! Maar Bazikone{noobat} raa {abs(jadval[index_location[noobat]])} khaane nish zad")
        index_location[noobat] += jadval[index_location[noobat]]

    print(f"Bazikone{noobat} dar khaane {index_location[noobat]} gharar darad")