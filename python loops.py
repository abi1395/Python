#python for loops

fruits = ["apple","banana","berry"]
for x in fruits:
    print(x)
    
#looping through string
for x in "banana":
    print(x)

#the break statement
for x in fruits:
    print(x)
    if x == "banana":
        break 


for x in fruits:
    if x == "banana":
        break
    print(x)
    
#the continue statement
for x in fruits:
    if x == "banana":
        continue
    print(x)
    
#range function
for x in range(6):
    print(x)
    
for x in range(2,30,3):
    print(x)

#else in for loop
for x in range(6):
    print(x)
else:
    print("done and dusted")
