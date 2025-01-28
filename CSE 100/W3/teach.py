import math
length_squ = float(input('What is the length of a side of the square? '))
area_squ = length_squ **2
print (f'The area of the square is: {area_squ}')
length_rec = float(input('What is the length of the rectangle? '))
width_rec = float(input('What is the width of the rectangle? '))
area_rec = length_rec * width_rec
print (f'The area of the rectangle is {area_rec}')
radius_cir = float(input('What is the radius of the circle? '))
area_cir = 3.14 * (radius_cir**2)
# OR area_cir = math.pi * (radius_cir**2)
print (f'The area of the circle is {area_cir}')


