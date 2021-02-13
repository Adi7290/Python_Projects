"""Write a program to enter the marks of a student in four subjects . Then Calculate the total and aggregate , and display the grade obtained by the student .
if the student scores an aggregate greater than 75%.
Then the grade is distinction. If aggregate is 60>= and <75,
then the grade is first division.
if aggregate is 50>= and <60,then the grade is second division.
If aggregate is 40>= and <50,Then the grade is third division . Else the grade is fail"""
mark1 = int(input('Enter the marks obtained in English:\t'))
mark2 = int(input('Enter the marks obtained in Hindi:\t'))
mark3 = int(input('Enter the marks obtained in Mathmatics:\t'))
mark4 = int(input('Enter the marks obtained in Science:\t'))
total_mark = mark1+mark2+mark3+mark4
average =total_mark/4
print(f'The total marks obtained by the student is  :\t {total_mark}')
print(f'The Total average of the marks is :\t {average}')
if average >75:
    print('The Student has marked an distinction')
elif average >=60 and average<75:
    print('The student has first grade and first division')
elif average>=50 and average<60:
    print('The Student has second division and second grade')
elif average >=40 and average<50:
    print('The student has third division and third grade')
elif average<40:
    print('The student is in fail')
else:
    print('Wrong Input')
