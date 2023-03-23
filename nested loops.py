#nested loops- loop inside a loop

adj = ["red","small","sour"]
fruits = ["apple","fig","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)


import sys
for i in range(1,11):
    for j in range(1,11):
        k = i*j
        print(k,end=' ')
        print()
        
