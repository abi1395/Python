#python conditional statement
#equals a==b
#not equals a!=b
#less than a<b
#greater than a>b
#less than or equal to a<=b
#greater than or equal to a>=b


#if statement
a = 50
b = 100
if b>a:
    print("b is greater than a")

#indentation- refer to space at the beginning of code line
if b>a:
    print("b is greater than a")


#elif- if previous condition is not true, then try this condition
a = 25
b = 25
if b>a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#else- 
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    

#short hand if
a = 50
b = 25
if a > b: print("a is greater than b")

#short hand if else
print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else  print("B")


#and
a = 20
b = 10
c = 25
if b > a and b > c:
    print("both the conditions are true")


#or
a = 20
b = 10
c = 25
if b > a or b < c:
    print("atleast one condition is true")
    
          

    
