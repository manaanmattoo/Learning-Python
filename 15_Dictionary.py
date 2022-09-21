# dict Syntax

mydict = {
    "Manaan" : "Papa",
    "Huzaif" : "Zanaan",
    "Danish" : "Mangul",
    "Bilal" : "Mouj",
    "Molvi" : "Hindustanas beni lyaath",
    "sum" : [ 1,20,203,50,0 ],
    "anotherdict" : {"House" : "room", # nesting dicttionaries using this syntax
    'Door' : 'window'} 
}
# NOTE : Single or double - both colons can be used in the print or my dict syntax 
# Here Manaan is the key & Papa is the value

print("The Value to the entered key is", mydict["Molvi"]) #Using  print(dicttionaryname['keyname'])
print("The Value to the entered key is", mydict["sum"]) # printing list
print("The Value to the entered key is", mydict["anotherdict"]) # using nested dict as a key
print("The Value to the entered key is", mydict["anotherdict"]["House"])#Using  print(dicttionaryname['keyname']['key name of nested dict'])

# Dict Methods 

print(mydict.keys())  # prints all the keys in the dict
print(mydict.values()) # prints all the values in the dict
print(mydict.items()) # prints all (key, value) with it's values in the dict
print(list(mydict.keys()))  # Typecastes data type into list, like using int, str etc

# Updating Dict

updatedict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "Manaan": "A Coder"
}
mydict.update(updatedict) # Updates the dictionary by adding key-value pairs from updateDict
print(mydict)

print(mydict.get("Manaan")) # Prints value associated with key "Manaan"
print(mydict["Manaan"]) # Prints value associated with key "Manaan"

# The difference between .get and [] sytax in Dictionaries?
print(mydict.get("Manaan2")) # Returns None as Manaan2 is not present in the dictionary
print(mydict["Manaan2"]) # throws an error as Manaan2 is not present in the dictionary