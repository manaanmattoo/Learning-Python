history = '''a succession of Hindu dynasties ruled \nover the region from the 7th\\14th centuries.\nAfter the seventh century, significant\t developments took place in Kashmiri\'s Hinduism.'''
print(history)

#String Functions
print(len(history))    #states length of a string (Counts number of characters)
print(history.endswith("Kashmiri Hinduism."))    # states true or flase if the string ends with the same data
print(history.count("Kashmiri"))     # To Find the number of times a word/ an alphabet is used
print(history.capitalize())      # captalises the first letter of the sentence .
print(history.find("region")) # states the index number of the word you're searching for
print(history.replace("Hindu", "Islam"))


# Using Espace Sequences
# \n   - puts the sentence in next line
# \t   - inserts tab space
# \'   - inserts single quote ( used when using single quote string) 
# \\   - used to insert a slash in the string