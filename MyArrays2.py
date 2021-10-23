import numpy as np


#ROWS = each student (student0, student1, student2, student3)
#COLS = each test (test0, test1, test2)
grades = np.array([[87, 96, 70], 
                    [100, 87, 90], 
                    [94, 77, 90], 
                    [100,81,82]])

student1 = grades[1]

student0_test1 = grades[0,1]

students0_1 = grades[0:2] 
#upper bound not included - just 0 and 1

students1and3 = grades[[1,3]]
#double brackets makes it just the row, not columns

students1and3_test2 = grades[[1,3], 2]

all_students_test0 = grades[:,0]

all_students_test1_2 = grades[:,1:3]

all_students_test0and2 = grades[:,[0,2]]


'''Create an array of 12 grades'''


grades = np.random.randint(60,101,12).reshape(3,4)
#numbers between 60 and 100; picks 12 numbers
#reshape into 3 rows and 4 columns 

grades.mean()

#avg by col
grades.mean(axis=0)

#avg by row
grades.mean(axis=1)


numbers = np.arrange(1,6)


#SHALLOW COPY:
numbers_view = numbers.view()

numbers[1] *= 10

#changes original value too:
numbers_view[1] /= 10

numbers_slice = numbers[0:3]

numbers[1] *= 20



#DEEP COPY:
numbers_copy = numbers.copy()

numbers[1] *= 10


grades = np.array([[87,96,70], [100,87,90]])


#reshape method produces a shallow copy:
grades_reshaped = grades.reshape(1,6)

grades.resize(1,6)


#flatten creates a deep copy:
flattened = grades.flatten()



#ravel creates a shallow copy:
raveled = grades.ravel()

raveled[0] = 100

flattened[1] = 100


grades = np.array([[87,96,70], [100,87,90]])
grades.T

grades2 = np.array([[94,77,90],[100,81,82]])

#add more columns:
h_grades = np.hstack((grades, grades2))

#add more rows:
v_grades = np.vstack((grades, grades2))


print()