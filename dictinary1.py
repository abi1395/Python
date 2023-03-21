#dictionary

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)



#accessing items
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict["brand"])



#changevalues
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["year"] = 2022
print(thisdict)


#loop through dictionary
#print all items one by one (left side)
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
for x in thisdict:
        print(x)


#print all items one bye one (right side)
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
for x in thisdict:
    print(thisdict[x])
    


#loop through both keys and values
for x,y in thisdict.items():
    print(x,y)


#to check of key exists in dictionary
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
if "model" in thisdict:
    print("yes, 'model' is one of the keys in the thisdict dictionary")



#dictionary length
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(len(thisdict))


#adding items
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["color"] = "red"
print(thisdict)


#removing items
#pop method
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.pop("model")
print(thisdict)

#pop item method- removes last inserted items 
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.popitem()
print(thisdict)


#del keyword
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
del thisdict["model"]
print(thisdict)


#clear keyword
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.clear()
print(thisdict)







    

