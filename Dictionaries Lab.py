

#Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.

PhoneBook = {'0568323222': 'Amal' , '0522222232': 'Mohammed' , '0532335983': 'Khadijah' , '0545341144': 'Abdullah' , '0545534556': 'Rawan' , '0560664566': 'Faisal' , '0567917077': 'Layla' }

NumO = input('Which Number Would You like to search about? ')

#- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
#- If the number is less or more than 10 numbers, print "This is invalid number".
#- If the number contains letters or symbols, print "This is invalid number".

if len(NumO) != 10:
    print("This is invalid number")

elif NumO.isalnum() == False:
    print("This is invalid number")

elif NumO in PhoneBook.keys():
    print("The owner of the number is : ", PhoneBook[NumO])
    
elif NumO not in PhoneBook.keys():
    print("Sorry, the number is not found")




