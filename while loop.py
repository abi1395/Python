#while loop- executes statements as long as condition is true

i = 1
while i < 6:
    print(i)
    i += 1
    
#break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#continue statement
i =0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
