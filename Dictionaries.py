## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 

import numbers


phonebook={'0568323222':'Amal',
'0522222232':'Mohammed',
'0532335983':'Khadijah',
'0545341144':'Abdullah',
'0545534556':'Rawan',
'0560664566':'Faisal',
'0567917077':'Layla'}

number=input("enter the number ?")

##- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
##- If the number is less or more than 10 numbers, print "This is invalid number".
##- If the number contains letters or symbols, print "This is invalid number".

if len(number) !=10:
    print("This is invalid number")

elif number.isalnum()== False:
    print("This is invalid number")

elif number in phonebook.keys():
    print("the owner of the number:",phonebook[number])

else:
    print("Sorry, the number is not found")

## Q2:Write a function that receives a list containing the following numbers : 

def sortlist(num_list:list):
    return num_list.sort(reverse=True)
num_list= [5, 0, 34, 9, 0, 13, 8]
sortlist(num_list)
print(num_list)


