#Write a program to calculate the distance between 2 coordinates or points
x1 = (int(input("Enter the coordinate of first point x:\t")))
x2 = (int(input("Enter the coordinate of second point x:\t")))
y1 = (int(input("Enter the coordinate of first point y:\t")))
y2 = (int(input("Enter the coordinate of second point x:\t")))
distance = ((x2-x1)**2+(y2-y1)**2)**0.5
print(distance)
print(f'The entered coordinates were {x1}  {x2}  {y1}  {y2}')
