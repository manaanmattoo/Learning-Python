from logging import logMultiprocessing
from re import L


# For Loop
'''
l = [1,7,8]
for item in l:
    print(item)

'''
# Range function in if loop
'''

for i in range(1,8,2): # here 1 is the start , 8 is the stop and 2 is the step (Slicing)
    print(i)

'''
#using else in if loop
'''
for i in range(1,8):
    print(i)
else:
    print("Done")
'''  
# using break statement in if loop
'''
for i in range(1,11): # will start the range from 1 and end at 11( prints only till 10 : n-1 )
    print(i)
    if i == 7: 
        break # will exit the loop at printing 7 
'''

# using continue statement in if loop

'''
for i in range(1,11):
  #  print(i) # for continue use it after using continue statement
    if i == 7: # will skip 7 when printing
        continue
    print(i) # type print at end like this

'''

# using pass statement in if loop
for i in range(1,11):
    pass # tells python to do nothing
    print(i) 


