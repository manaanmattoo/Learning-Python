# Q1
'''

l1 = input("Enter the name of fruit No.1 \n")
l2 = input("Enter the name of fruit No.2 \n")
l3 = input("Enter the name of fruit No.3 \n")
l4 = input("Enter the name of fruit No.4 \n")
l5 = input("Enter the name of fruit No.5 \n")
l6 = input("Enter the name of fruit No.6 \n")
l7 = input("Enter the name of fruit No.7 \n")

myfruitlist = [l1,l2,l3,l4,l5,l6,l7]

print("The name of Fruits Entered is", myfruitlist)'''

# Q2
'''

l1 = int(input("Enter the marks for Student 1 \n"))
l2 = int(input("Enter the marks for Student 2 \n"))
l3 = int(input("Enter the marks for Student 3 \n"))
l4 = int(input("Enter the marks for Student 4 \n"))
l5 = int(input("Enter the marks for Student 5 \n"))
l6 = int(input("Enter the marks for Student 6 \n"))

studentlist = [l1,l2,l3,l4,l5,l6]
studentlist.sort() # Do not create a varaible for list methods

print(studentlist)
'''
# Q3 Check if the value of tuple can be changed .
'''
t1 =(1,2,3,4,5)
t1[0] = 50 # A tuple value can't be replaced
print(t1) '''

# Q4 sum the list  numbers

l1 = [56,54,200,500,700,72222]
print("the sum of the list is",l1[0]+l1[1]+l1[2]+l1[3]+l1[4]+l1[5]) # Long / Unusable method
print("the sum of the list is",sum(l1)) # Method that should be used

# Q5

a = [7,0,8,0,66,0,66,0,8] # used [] for list 
print("Number 0 occurs",a.count(0),"times in the given list") # here i am printing the number of occurance of the digit 0 in the given list.

