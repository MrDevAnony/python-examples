# نرخ هر ساعت کاری
price = 100000

# دریافت تعداد ساعت از کاربر
worked_time = int(input("Enter your work time in one day: "))

# فانکشن محاسبه حقوق
def work_price (price, worked_time):
    # محاسبه دو برابری تایم اضافه کاری و جمع کردن با حقوق پایه در صورت اضافه کاری
    if worked_time > 8:
        bonus_time = worked_time - 8
        last_price = (bonus_time * price * 2) + (8 * price) 
    else:
        # در صورت نداشتن اضافه کاری، حقوق به روال عادی محاسبه می‌شود
        last_price = price * worked_time
    return last_price

# فراخوانی فانکشن + پرینت نتایج
print(f"Your Last Price is: {work_price(price, worked_time):,}")