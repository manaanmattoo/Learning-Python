# Q1 
'''
from msilib.schema import Condition


a = int(input("Enter the Ist number i.e A \n"))
b = int(input("Enter the 2nd number i.e B \n"))
c = int(input("Enter the 3rd number i.e C \n"))
d = int(input("Enter the 4th number i.e D \n"))

if a>b and a>c and a>d:
  print(" A is the Greatest number i.e : ", a)

elif b>a and b>c and b>d:
  print(" B is the Greatest number i.e : ", b)

elif c>a and c>b and c>d:
  print(" C is the Greatest number i.e : ", c)

elif d>a and d>b and d>c:
  print(" D is the Greatest number i.e : ", d)

else:
    print("None of Conditions are true")

'''

# Q2

'''
science = int(input("Enter Marks for Science Subject : \n"))
maths = int(input("Enter Marks for Science Subject : \n"))
english = int(input("Enter Marks for Science Subject : \n"))

if (science<33 or maths<33 or english<33):
    print("You have failed the Examination as one or more of your subject is having less than 33%")
elif(science+maths+english)/3 <40: #use divide or percentage formula here
    print("You have failed the the Examination as you lack total 40%")
else:
    print("Congratulations ! You have passed the Exam.")

'''

#Q3
'''
text = input("Enter the Text :\n")

a =  "make alot of money"
b = "click this"
c = "buy now"
d = "subscribe this"

if (a in text or b in text or c in text or d in text):
    print("This text is containing spam keywords")
else:
    print("No Spam Found and The Entered Text is: \n", text)
'''
#-----------------------------------------OR--------------------------
'''
if a in text:
    print("This text is containing spam keywords")
elif b in text:
    print("This text is containing spam keywords")
elif c in text:
    print("This text is containing spam keywords")
elif d in text:
    print("This text is containing spam keywords")
else:
    print("No Spam Found and The Entered Text is: \n", text)
'''
#-----------------------------------------OR--------------------------
'''
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")

'''
# Q4
'''
username = str(input("Enter your username : \n"))

if  len(username) > 10:
    print("The Username is of 10 or more characters")

else:
    print("The Username contains less than or equal to 10 characters")

'''
# Q5
'''

namelist = ["Manaan", "Burhan", "Huzaif", "Mangloo", "Bilal"]
name= str(input("Enter the Name to Check :\n"))

if name in namelist:
    print("The name is on the list ")
else:
    print("The name is not in the list")

'''

# Q6
'''
marks = int(input("Enter the marks Out of 100 : \n"))

if   marks <= 90:
  grade = "Excellent A+"
elif marks <= 80:
  grade = "Grade A"
elif marks <= 70:
  grade = "Grade B"
elif marks <= 60:
  grade = "Grade C"
elif marks <= 50:
  grade = "Grade D"
else:
  grade = "Failed"

print("Your result is : "+ grade)
'''

# Q7
'''
Text = str(input("Enter you text here : \n"))

if "Manaan" in Text or "manaan" in Text:
    print('The Text Contains the Name :\n "Manaan"')
else:
    print("The Text Doesn't contain the name :\n 'Manaan'")

'''