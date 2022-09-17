from operator import truediv


a = 60
b = 20

#Arithmatic Operators =, -, +, /, *
print ("the value of a+b =", a + b)
print ("the value of a-b =", a - b)
print ("the value of a*b =", a * b)
print ("the value of a/b =", a / b)

#Assignment Operators =, -=, +=
print ("the value of a==b =", a==b)

#Examples 
a-=20
print(a)

a+=60
print(a)

a/=40
print(a)

#Comparison Operators

print ("the value of a<b =", a<b)
print ("the value of a>b =", a>b)
print ("the value of a<=b =", a<=b)
print ("the value of a>=b =", a>=b)
print ("the value of a==b =", a==b)
print ("the value of a!=b =", a!=b)

#Examples
#using comparison operaters ==, >=, <=, !=(not equal to)

p = (10>=7)
print ("the value of p is", p)

q = (20<=10)
print("the value of p is", q)

r = (10!=2)
print ("the value of p is",r)

#Logical Operators ( and, or , not)
bool1=True
bool2=False
print("The value of bool1 and bool12 is", (bool1 and bool2))
print ("The value of booll or bool2 is", (bool1 or bool2))
print("The value off not bool2 is", (not bool2))