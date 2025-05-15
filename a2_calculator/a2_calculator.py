def calculator():
    """این تابع یک ماشین حساب ساده را پیاده‌سازی می‌کند."""
    try:
        # وردی ها
        first_number=int(input("Enter your first number: "))
        second_number=int(input("Enter your second number: "))
        operator =input(f"Choose an operator: \n+ for addition \n- for subtraction \n/ for division \n* for multiplication \nP for power \nD for division remainder "
                    "\nWhich operator do you want: ").upper()

        # تعریف عملگرها
        if operator == "+":
            print(f"{first_number} + {second_number} = {first_number + second_number}")

        elif operator == "-":
            print(f"{first_number} - {second_number} =  {first_number - second_number}")

        elif operator == "*":
            print(f"{first_number} * {second_number} = {first_number * second_number}")

        elif operator == "P":
            print(f"{first_number} ** {second_number} = {first_number ** second_number}")

        elif operator == "D":
            if second_number==0 :
                print("*** We can't divide by 0! ***")
            else:
                print(f"The remainder is divided by ({first_number} / {second_number}) = {first_number % second_number}")

        elif operator == "/":
            if second_number==0 :
                print("*** We can't divide by 0! ***")
            else:
                print(f"{first_number} / {second_number} = {first_number / second_number}")
        else:
            print("Invalid operator!")

    # اگر کاربر خطایی را انجام دهد آن خطا نمایش داده میشه
    except Exception as e:
            print(f"Oops! Somthing wrong: {e}")

    print("_"*30)

# صدا زدن تابع ماشین حساب
calculator()