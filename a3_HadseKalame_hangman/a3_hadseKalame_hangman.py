#  پروژه حدس کلمه یا هنگ من با شرایط زیر انجام دهید

# باید شما در کنار پاین پایتونتون یه فایل از نوع txt وجو داشته باشه که منبع کلمات باشه
# و بشه داخلش کلمه اضافه کرد و کلمات رو با استفاده از ( , ) از هم داخل فایل جدا کنید 
# بعد از اون داخل برنامه این فایل رو باز کنید
# و کلمات رو از داخل فایل بخونید
# و کلمات رو داخل لیست ذخیره کنید  
# تابعی بنویسید که  با استفاده از کتابخانه رندوم به صورت تصادفی یکی از کلمات این لیست رو انتخاب کند و return  کند  
# حالا به تعداد حروف کلمه ای که انتخاب شده به کاربر خط چین نمایش بدید
# برای مثال اگر کلمه انتخاب شده yazd بود باید برای کاربر - - - - نمایش داده بشه ( نحوه نمایش به عهده خودتونه ) 
# حالا از کاربر باید بخواید تا یک کاراکتر وارد کنه 
# اگر اون کاراکتر داخل کلمه بود
# باید در جای درست به جای خط چین قرار بدید 
# و خط چین هارو به کاربر نمایش بدبد( مثال : اگر کاربر a وارد کرده بود نمایش خط چین ها به این صورت میشود - - a -) 
# و اگر کاراکتر وارد شده داخل کلمه انتخاب شده نبود چیزی جایگذاری نمیشه و به همون شکل قبل خط چین ها به کاربر نمایش داده میشه  
# گرفتن حرف از کاربر تا جایی باید تکرار شود که کاربر تمام کاراکتر های کلمه انتخاب شده رو حدس بزنه  

# امتیازی : به بازی بالا شانس  هم اضافه کنید برای مثال اگر کاربر سه شانس داشت و حرف انتخابی کاربر داخل کلمه نبود یکی از شانس های اون کم بشه 
# و در اخر اگر شانس هاش تموم شدد و کلمه رو کامل نکرده بود به اون پیامی برای باختن نمایش بده  
# باید بازی طوری طراحی باشه کاربر هر چند بار که خواست بازی رو انجام بده 
# و وقتی بازی رو خواست پایان برسونه تعداد بازی های که برده هست در یک فایل txt در کنار فایل پایتون ذخیره شود  

# موفق باشید

import random

# نوشتن فایلی با اسامی دختر و پسر
f = open("hamgman.txt", "w")
f.write("*boysName*\n")
f.write("ali, amir, hossein, mohammad\n")
f.write("shahram, shayan, roohan, matin\n\n")
f.write("*girlsName*\n")
f.write("fateme, zahra, mahsa, sara, mahla\n")
f.close()

# خواندن فایل
with open("hamgman.txt", "r") as f:
    lines = f.readlines()
boys_names = []
girls_names = []
current_category = ""

# اوردن و دسته بندی اسامی از فایل به داخل لیست: لیست دختر یا لیست پسر
for line in lines:
    line = line.strip()
    if line == "*boysName*":
        current_category = "boys"
    elif line == "*girlsName*":
        current_category = "girls"
    elif line:  # اگر خط خالی نباشد
        if current_category == "boys":
            boys_names.extend(line.split(", "))
        elif current_category == "girls":
            girls_names.extend(line.split(", "))

# ملزومات تابع رندوم
tedade_bord = []
tedade_bakht = []
tedad_avalie_k = 0
tedad_avalie_o = 0


# از اسامی دختر یا پسر به صورت رندوم اسمی انتخاب میشه
def random_name():
    if typename == "boys":
        randomboys = random.choice(boys_names)
        return randomboys
    if typename == "girls":
        randomgirls = random.choice(girls_names)
        return randomgirls


# تا زمانی که فرد وای را وارد کنه بازی ادامه پیدا میکنه            
while True:
    edame_baazi = input("Do you want hangman game? Y / N: ")
    if edame_baazi == "N":
        print("Hoping to meet you.")
        print("Your game results are in file 'natyege baazi.txt'.")
        break
    if edame_baazi == "Y":
        typename = input("What kind of name do you want for hangma game ( boys / girls )? ")

        # ملزومات بازی که شامل تعداد حدس و.. هستش    
        random_namee = list(random_name())
        tedade_hads = len(random_namee)
        khotot = tedade_hads * "_"
        list_khotot = list(tedade_hads * "_")
        print(f"{khotot}")

        # بدنه بازی
        for i in range(tedade_hads):
            print()

            hadse_harf = input(f"Enter {i + 1}th choice of {tedade_hads - i}: ")

            # بدنه اصلی بازی
            if "_" in list_khotot:
                for k in range(len(random_namee)):
                    j = random_namee[k]
                    if j == hadse_harf:
                        list_khotot[k] = hadse_harf
                print("".join(list_khotot))

            # ثبت برد 
            if "_" not in list_khotot:
                tedad_avalie_o += 1
                tedade_bord.append(tedad_avalie_o)
                print("YOU WON")
                break

                # ثبت باخت
            elif "_" in list_khotot and i + 1 == tedade_hads:
                print("GAME OVER")
                tedad_avalie_k += 1
                tedade_bakht.append(tedad_avalie_k)
                break

        print()

    # ایجاد فایل گزارش نتایج بازی        
if tedade_bord or tedade_bakht:
    f = open("natyege baazi.txt", "w")
    f.write(f"Tedade bord: {str(tedade_bord)}\n")
    f.write(f"Tedade baakht: {str(tedade_bakht)}\n")