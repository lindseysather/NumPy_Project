## Numpy Exercise 2
import numpy as np

## This array documnets the last 5 sales for each of Superstore's four cash registers. 
#                       
salesArray = np.array([[150.68,207.99,107.88,58.99,60.59],
                        [20.89,98.99,258.62,19.76,101.59],
                        [70.66,190.10,134.54,200.14,15.59],
                        [10.52,201.59,140.55,13.99,45.98]])

## Step 1: Print the total sales for the store.
print("\n-----------------------------------------------   STEP ONE   -----------------------------------------------\n")

print("Total Sales: $", salesArray.sum(), sep='')

## Step 2: What was Superstore's smallest and largest sale? Print them.
print("\n-----------------------------------------------   STEP TWO   -----------------------------------------------\n")

print("Smallest Sale: $", salesArray.min(), "\nLargest Sale:  $", salesArray.max(), sep='')

## Step 3: Print an array that will show which sales are greater than or equal to $100.
print("\n-----------------------------------------------   STEP THREE  -----------------------------------------------\n")

bigSales = salesArray >= 100
print("Sales >= $100:\n", bigSales, sep='')

## Step 4: Print the total sales for each register.
print("\n-----------------------------------------------   STEP FOUR   -----------------------------------------------\n")

registerSales = salesArray.sum(axis=1)
print("Register Sales Array:", registerSales)
print()
print("Register 1 Sales: $", registerSales[0], sep='')
print("Register 2 Sales: $", registerSales[1], sep='')
print("Register 3 Sales: $", registerSales[2], sep='')
print("Register 4 Sales: $", round(registerSales[3], 2), sep='')

## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. Each sale is subject to a 2% credit card fee.
#           Using the salesArray, create a new array that stores the 2% fee for each sale and register. Print the array and then print the total fees.
print("\n-----------------------------------------------   STEP FIVE  -----------------------------------------------\n")

feesArray = salesArray * 0.02
print("Credit Card Fees:\n", feesArray)
print("\nTotal Fees: $", round(feesArray.sum(), 2), sep='')

## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. Store this in a new array and print it.
print("\n-----------------------------------------------   STEP SIX  -----------------------------------------------\n")

profitsArray = salesArray - feesArray
print("Profit After Fees:\n", profitsArray)

## Step 7: Print the sales only for the second and fourth cash register
print("\n-----------------------------------------------   STEP SEVEN  -----------------------------------------------\n")

print("Sales for 2nd and 4th Registers:\n", salesArray[[1,3]])

## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister. Add the new register to the original array. Print the updated salesArray.
print("\n-----------------------------------------------   STEP EIGHT  -----------------------------------------------\n")

newRegister = np.array([17.89,13.59,107.89,176.88,56.78])

salesArray = np.vstack((salesArray, newRegister))
print("5th Register Added:\n", salesArray)

## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly. The sale should have been $20.14. Update the array to correct this error.
#           Print the array before and after the update to see the change.
print("\n-----------------------------------------------   STEP NINE  -----------------------------------------------\n")

print("Register 3 With Error:\n", salesArray)
salesArray[2][3] = 20.14
print("\nRegister 3 Error Resolved:\n", salesArray)

