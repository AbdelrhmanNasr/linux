
#a = int (input ("give me the frist number "))
#b = int (input ("give me the second number "))

#print (a+b ,a-b,a*b,a/b,a&b,a|b,a^b,a==b,a<b,a<b)
#take values from sensor 
val1 = int (input("enter th values "))
val2 = int (input("enter th values"))
val3 = int (input("enter th values "))
valuesList= [val1,val2,val3]
valuesTuble= (val1,val2,val3)
valuesDic=  {
            "value1" :val1,
            "value2" :val2,
            "value3" :val3
            }

print(valuesList)
print(valuesTuble)
print(valuesDic)