import numpy as np
import random


arr01 = np.array([[1,2,3],
                [4,5,6]])

#2D - rows and columns; 2 rows and 3 columns 
#1,2,3 represent 1st row
#4,5,6 represent 2nd row

arr02 = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

for row in arr01:
    print(row)
    for col in row:
        print(col, end=' ')
        #end=' ' changes end character from \n to a space
    print()

for i in arr01.flat:
    #flattens numbers - no longer in columns and rows
    print(i)

arr03 = np.zeros(5)

arr04 = np.ones((2,4), dtype=int)
    #2,4 is number of rows and columns

arr05 = np.full((3,5),13)

print()


a = np.array([[random.randint(1,10) for i in range(5)],[random.randint(1,10) for i in range(5)]])
print(a)

b = np.array(np.random.randint(1,10,size=(2,5)))
print(b)

arr06 = np.arange(5)

arr07 = np.arange(5,10)
#numpy arange = normal python range

arr08 = np.arange(10,1,-2)

arr09 = np.linspace(0.0, 1.0, num=5)

arr10 = np.arange(1,21).reshape(4,5)


num01 = np.arange(1,6)

num02 = num01*2

num03 = num01**3

num04 = num01 * num02

num05 = num01 > 13

num06 = num03 > num01


grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100,81,82]])

print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())

#calculate average on all rows for each column (test 1):
grades_by_exam = grades.mean(axis=0)

#calculate average on all columns for each row (student 1):
grades_by_student = grades.mean(axis=1)

num07 = np.array([1, 4, 9, 16, 25, 36])
num08 = np.sqrt(num07)

num09 = np.array([10,20,30,40,50,60])

num10 = np.add(num07,num09)
#same as
num10 = num07 + num09

num11 = np.multiply(num09, 5)
#same as
num11 = num09 * 5


num12 = num09.reshape(2,3)
num13 = np.array([2,4,6])

num14 = np.multiply(num12, num13)
#BROADCASTING: APPLIES SOMETHING TO EVERYTHING
#number of columns have to match (not rows)

print()