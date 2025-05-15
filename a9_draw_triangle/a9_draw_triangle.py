# رسم مثلث قائم الزاویه
def triangle(high):
    for i in range(1,high+1):
        print(i *"*")
triangle(5)

# خروجی:
# *
# **
# ***
# ****
# *****

# _______________________
# رسم مثلث متساوی الاضلاع:
def triangle(height):
    for i in range(1,height+1):
        print((height-i)*" ", (i+(i-1))*"*" )

triangle(5)
#
# # خروجی:
# #        *
# #       ***
# #      *****
# #     *******
# #    *********

# _______________________

def draw_equilateral_triangle(height):
    for i in range(height):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (height - i )
        print(spaces + stars )

# تعیین ارتفاع مثلث (تعداد ردیف ها)
triangle_height = 5
draw_equilateral_triangle(triangle_height)