#list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#access items
print(thislist[1])

#change item value
thislist[1] = "blackcurrant"
print(thislist)

#loop through list
for x in thislist:
    print(x)

    
#check if items exists
if "banana" in thislist:
    print("yes, banana is n this fruit list")

#list lenghth
print(len(thislist))

#add items
thislist.append("blackcurrant")



#pop method
thislist.pop()
print(thislist)

thislist.pop(1)
print(thislist)

#del keyword
del thislist[0]
print(thislist)

#clear method
thislist.clear()
print(thislist)
