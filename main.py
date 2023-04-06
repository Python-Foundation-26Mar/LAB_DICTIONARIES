## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.
Phone_Book = {'0568323222': 'Amal' , '0522222232': 'Mohammed' , '0532335983': 'Khadijah' , '0545341144': 'Abdullah' , '0545534556': 'Rawan' , '0560664566': 'Faisal' , '0567917077': 'Layla' }
number = input('Enter the phone number ? ')

#- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
#- If the number is less or more than 10 numbers, print "This is invalid number".
#- If the number contains letters or symbols, print "This is invalid number".

if len(number) != 10:
    print("This is invalid number")

elif number.isalnum() == False:
    print("This is invalid number")

elif number in Phone_Book.keys():
    print("The owner of the number is : ", Phone_Book[number])

elif number not in Phone_Book.keys():
    print("Sorry, the number is not found")


# Q2: 

Numberslist = [5, 0, 34, 9, 0, 13, 8]
Numberslist.sort(reverse = True)
print(Numberslist)
