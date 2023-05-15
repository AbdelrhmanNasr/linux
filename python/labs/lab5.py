
a = int (input ("give me the 1 number "))
b = int (input ("give me the 2 number "))
c = int (input ("give me the 3 number "))
d = int (input ("give me the 4 number "))
e = int (input ("give me the 5 number "))

list= [a,b,c,d,e]

r = int (input ("give me the number "))

if r in list:
    print("exist")
else:
    print("not exist")
