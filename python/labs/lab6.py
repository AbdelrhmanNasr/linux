print ("please select choise ")
print ("1- find  ")
print ("2-count ")

choise = int (input("enter choise "))
if choise == 1:
    txt = "Hello, welcome to my world."
    x = txt.find("welcome")
    print(x)
    
elif choise == 2:
    txt = "I love apples, apple are my favorite fruit"
    x = txt.count("apple")
    print(x) 
else:
    print("Invalid Input.")