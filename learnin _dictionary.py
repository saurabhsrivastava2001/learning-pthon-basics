#declaration of a dictionary
this_dict= {
    "brand":"ford",
    "model": "mustang",
    "year":1964
}

#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

print("my dictionary is---- ", this_dict)

#printing the values associated with the keys in the dict

print("the value of brand key is---- ", this_dict["brand"])

#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Dictionaries cannot have two items with the same key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print("the dictionary has no duplicate keys  if we assign two or mor same keys the value will be reassign",thisdict)
#-----------------------------------------------

#dictionary funcions

#1. len() function gives the length of the dictionary
print("the length of dictionary is :", len(thisdict))
#the values in the dictionary cacn have any data type



# the dict constructor
thisdict2 = dict(name = "John", age = 36, country = "Norway")
print(thisdict2)


#----------------------------------------
"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List -is a collection which is ordered and changeable. Allows duplicate members.
Tuple -is a collection which is ordered and unchangeable. Allows duplicate members.
Set -is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary -is a collection which is ordered** and changeable. No duplicate members.
"""

#--------------------------------------------

#access dict items
#You can access the items of a dictionary by referring to its key name, inside square brackets:

y=thisdict["model"]
print(y)

#get the value of the model key
z=thisdict.get("model")

#the  key() method will give all the keys of dict
allkeys= thisdict.keys()
print(allkeys)

#adding items in dict--
thisdict["color"]= "white"
print(thisdict)


#values() will give all the values in the dict
x=thisdict.values()
print(x)

#get the list of all items
x=thisdict.items()
print(x)

#--------------------------
#chec if a speciffic key present in dict--------
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#-------------------------------remove form a dictinary
#1.pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#2. ppopitems() will remove the last item from the dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#3. del keyword
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


#del can delete whoke dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
try:
    print(thisdict) #this will cause an error because "thisdict" no longer exists.
except :
    print(' thisdict has been deletd earlier')


#4. clear() --  clears the dict and make it empty
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
