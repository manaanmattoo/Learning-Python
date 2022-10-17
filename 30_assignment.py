# Q1
def greatest(n,b,m):
    if n>b and n>m:
        return (n)
    elif  b>n and b>m:
        return (b)
    else :
        return (m)
"""
a = int(input("Enter the number (1st) : "))
b = int(input("Enter the number (2nd) : "))
c = int(input("Enter the number (3rd) : "))
g = greatest(a,b,c) # using func

print(f"The greatest number among the input is {g}")
"""
# Q2
def farh(celsius):
    return (celsius * 1.8) + 32
"""
c = int(input("Enter the Celsuis Temp : \n")) # represting celsius here
f = farh(c)

print(f"The Conversion of {c}° Celsuis in Farh = {f}° Farh")
"""

# Q3
"""print("Hello", end=" ")
print("How", end=" ")
print("are", end=" ")
print("you?", end=" ")"""

# Q4
def Mysum(n):
  pass

#Q5
"""n = 3
for i in range(n):
    print("*" * (n-i))
"""
#Q6 inch to cms

def cm(inch):
    return inch * 2.54
"""
inch = int(input("Enter the inch measurement : "))
c = cm(inch)

print (f"The Conversion of {inch} Inches into Cms = {c} cm")"""

# Q7
def remove_str(sentence, word):
    newstr = sentence.replace(word , "")
    return newstr.string() # .string removes spaces before and after the sentnce
"""
n = "   hi my name is manaan    " #Here there's space before hi and after manaan
g = remove_str(n, "name")
print(g)
"""
# Q8
"""def multitab(n):
    for i in range(1,11):
        return (f"{n} x {i} = {n*i}")"""
# OR
def multitab(n):
    i = 1 
    while i <= 10:
        print (f"{n} x {i} = {n*i}")
        i = i + 1

tab = int(input("Please Enter a Number for it's Multiplication table: "))
g = multitab(tab)
print(g)
