# Q1
'''
hindidict = {
    'Naam': 'Name',
    'Kaam': 'work',
    'Daam': 'Price',
    'Khao': 'Eat'
 }

print("Words in HindiDict are : \n", hindidict.keys())

#getting input from user for searching the key

a= input("Enter the Hindi Word to get the meaning \n")
# print("The meaning of your Hindi Word is\n", hindidict[a])

print("The meaning of your Hindi Word is\n", hindidict.get[a]) # Return None as error if the word isn't there 
'''
# Q2
'''
n1 = int(input("Enter No.1 \n"))
n2 = int(input("Enter No.2 \n"))
n3 = int(input("Enter No.3 \n"))
n4 = int(input("Enter No.4 \n"))
n5 = int(input("Enter No.5 \n"))
n6 = int(input("Enter No.6 \n"))
n7 = int(input("Enter No.7 \n"))
n8 = int(input("Enter No.8 \n"))

set1 = {n1,n2,n3,n4,n5,n6,n7,n8}

print("Unique numbers in the given data are\n", set1)
'''

#Q3 Answer - Yes

'''
set1 = {18,"18"}
print(set1)
'''

# Q4
'''
s = set() # Emply set
s.add(20)
s.add(20.0)
s.add("20")

print(s)
print(len(s))
'''

# Q5
'''
s = {}
print(type(s))

'''

# Q6
'''
mydict = {} # Empty Dictionary

a = str(input("Enter the Key\n"))
b = str(input("Enter the value\n"))

a1 = str(input("Enter the Key\n"))
b1 = str(input("Enter the value\n"))

a2 = str(input("Enter the Key\n"))
b2 = str(input("Enter the value\n"))

mydict.update({
    a : b,
    a1 : b1,
    a2 : b2
    })

print(mydict.items())
'''

# Or

favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n")
d = input("Enter your favorite language Harshita\n")
favLang['shubham'] = a # here ['This is the key']
favLang['ankit'] = b
favLang['sonali'] = c
favLang['harshita'] = d
print(favLang)





