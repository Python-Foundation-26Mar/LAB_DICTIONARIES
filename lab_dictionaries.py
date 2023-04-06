'''
Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.
You can follow the table below:

Name	Number
Amal	0568323222
Mohammed	0522222232
Khadijah	0532335983
Abdullah	0545341144
Rawan	0545534556
Faisal	0560664566
Layla	0567917077

If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
If the number is less or more than 10 numbers, print "This is invalid number".
If the number contains letters or symbols, print "This is invalid number".
'''

# Q1
phone_book_dic = {"0568323222": "Amal", "0522222232": "Mohammed", "0532335983": "Khadijah", 
"0545341144": "Abdullah", "0545534556": "Rawan", "0560664566": "Faisal", "0567917077": "Layla"  }

phone = input("Enter your number : ")

# if is number
if phone.isdigit():
    # if 10 number
    if len(phone) == 10:
        # if the number exists
        if phone in phone_book_dic :
            print("the name is : ",phone_book_dic.get(phone))
        else:
            print("Sorry, the number is not found")
    else:
        print("This is invalid number")
else :
    print("This is invalid number")

'''
Q2:Write a function that receives a list containing the following numbers :
[5, 0, 34, 9, 0, 13, 8]
rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
'''
# Q2
list1= [5, 0, 34, 9, 0, 13, 8]

def zero_to_end(list2):
# storing all non zero values
    nonZeroValues = [x for x in list2 if x != 0]
 
# storing all zeroes
    zeroes = [j for j in list2 if j == 0]
 
# updating the list
    list2 = nonZeroValues + zeroes
    return list2

print(zero_to_end(list1))