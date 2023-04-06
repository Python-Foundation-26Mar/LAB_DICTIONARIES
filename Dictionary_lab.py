phoneBook = {
    '0568323222': 'Amal' ,
    '0522222232': 'Mohammed' ,
    '0532335983': 'Khadijah' ,
    '0545341144': 'Abdullah' ,
    '0545534556': 'Rawan' ,
    '0560664566': 'Faisal' ,
    '0567917077': 'Layla'
    }

phoneNumber = input('Enter the phone number: ')

# If the number is less or more than 10 numbers, print "This is invalid number"
if len(phoneNumber) != 10:
    print("This is invalid number")

# If the number contains letters or symbols, print "This is invalid number".
elif phoneNumber.isalnum() == False:
    print("This is invalid number")

# # If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
elif phoneNumber in phoneBook.keys():
    print("The owner of the number is : ", phoneBook[phoneNumber])

elif phoneNumber not in phoneBook.keys():
    print("Sorry, the number is not found")


# Q2:
def listing_numbers(numberList: list):
    return numberList.sort(reverse = True)

numberList = [5, 0, 34, 9, 0, 13, 8]
listing_numbers(numberList)
print("The answer is: " , numberList)