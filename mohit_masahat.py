# عدد پی: 3.14
p = 3.14

# دریافت شعاع دایره از کاربر
radius = float(input("enter the radius: "))

# فانکشن محاسبه محیط دایره
def perimeter_circle(radius):
    perimeter = radius * p * 2
    return perimeter

# فانکشن محاسبه مساحت دایره
def area_circle(radius):
    area = radius **2 * p
    return area

# فراخوانی فانکشن‌ها و پرینت ارقام محاسبه شده
print("The perimeter of the circle is: ", perimeter_circle(radius))
print("The area of the circle is: ", area_circle(radius))