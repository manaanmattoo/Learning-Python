# Sets in pyhton
'''
a = {1,2,3,4,1} # last 1 wontshow up as its being repeated . a set can not contain duplicate / repeatative elemets.

a.add((1,2,3,4)) # can add tuple to sets but not lists or dictionaries ( DS that can be changed cant be added to sets  )
# Creating an empty set
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

## Length of the Set
print(len(b)) # Prints the length of this set

## Removal of an Item
b.remove(5) # Removes 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop()) deletes random element from the set
print(b)
print(a)

'''
a={1,2,3,4}
# print(a.union({4,5,6})) # joins the both sets together . erases duplicate/ common elements data like 4 here
print(a.intersection({4,5,6})) # prints the common element in both sets joining together the sets.

