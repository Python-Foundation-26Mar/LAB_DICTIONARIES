PhoneBook ={'0568323222':'Amal',
            '0522222232':'Mohammed',
            '0532335983':'Khadijah',
            '0545341144':'Abdullah',
            '0545534556':'Rawan' , 
            '0560664566': 'Faisal' , 
            '0567917077': 'Layla' }

Num = input('Which Number you want to search ? ')


if len(Num) != 10:
    print("This is invalid number")

elif Num.isalnum() == False:
    print("This is invalid number")

elif Num in PhoneBook.keys():
    print("The owner is : ", PhoneBook[Num])
    
else:
    print("Sorry, the number is not found")