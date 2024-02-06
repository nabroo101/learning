#!/usr/python3
# this is our first script


Number1 = input("enter number 1: ")
Number1 = float(Number1)
Number2 = input("enter number 2: ")
Number2 = float(Number2)
Total = Number1 + Number2 # 
if Total == 15 :
    Number3 = input(" You are lucky , guess one more number : ")
    Number3 = float(Number3)
    Total2 = Total + Number3
    if Total2 == 20:
        print ( "YOU WIN!!")
    else : 
        print (" Thank you for playing:" + str(Total2))
        
else : 
    print ("your total is : " + str(Total))
print("checking branching github")
print("first_branch")