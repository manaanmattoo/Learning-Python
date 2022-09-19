#Q1.
'''name=input("What is your Name? ")
print("Good Afternoon, " + name) '''

#Q2.
'''
name=input("What is your Name")
_date=input("Enter the date")
print("Dear",name,"\nYou are Selected !\n",_date)
'''
#   or

#letter = '''Dear <NAME>,
#Congratulations ! You are Selected
#Thanks & Regards'
#Manaan Mattoo
#Date: <DATE>'''
#
#name=input("Enter Your Name\n")
#date=input("Enter Date\n")
#
#letter= letter.replace("<NAME>", name)
#letter= letter.replace("<DATE>", date)
#
#print(letter)

#Q3.1
'''
from dataclasses import replace


story = "You are Selected  ,We're Humans!"
st= story.find("  ")
st= story.replace("  ", " ")
print(st)
'''
    