# Q1 print multiplication table of the number taken input from usr from 1 to 10


num = int(input("Enter the number : \n"))
for i in range(1,11):
  #  print(str(num), "X" ,str(i), "=" , str(num*i))
#--------------------------------- or -------------------------------------------------
    print (f"{num} X {i} = {num*i}") # using f'{command}text {command}. We can use elements in string by using f and {}'


#----------------------------------or--------------------------------------------------

# Q2
"""
l1 = ["Harry", "Shoham", "Salman", "Rahul"]
for name in l1:
  if name.startswith("S"):
    print("Greeting ! , " + name)
"""

# Q3 Try myself Q1 - using while loop.

"""
num = int(input("Enter the Number:\n"))
mult_num = 1
while mult_num <=15:
  print("Here is your multiplication table\n"f"{num} x {mult_num} = {num * mult_num}")
  mult_num = mult_num + 1

"""
# Q4
"""
num = int(input("Enter the Number:\n"))
prime = True

for i in range(2, num):
  if num%i == 0:
    prime = False
    break

if prime :
  print("This is a Prime number.")
else:
  print("This is not a Prime number.")
"""
"""# Q5

n=int(input("Enter a number: "))
sum = 0
while(n > 0):
    sum = sum + n
    n=n-1
print("The sum of first n natural numbers is",sum)

# Q6"""
"""
n=int(input("Enter a number: "))
factorial = 1
for i in range(1, n+1):
  factorial = factorial * i
  print(f"The Factorial of {n} is : {factorial} ")"""

  