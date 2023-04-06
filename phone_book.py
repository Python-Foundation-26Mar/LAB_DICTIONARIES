''' phone book program that receives the phone number (Use Input to let the user provide the number), 
and returns the name of the owner.'''
#Q1

phone_book = {"0568323222" : "Amal" , "0522222232 ": "Mohammed","0532335983" : "Khadijah", "0545341144" :"Abdullah" , "0545534556" : "Rawan" , "0560664566" : "Faisal", "0567917077" : "Layla"}

phone_number = input("Enter a phone number: ")
if not phone_number.isdigit():
       print("This is invalid number use only number")

elif len(phone_number) < 10 or len(phone_number) > 10:
        print("This is invalid number")  


elif not phone_number in phone_book:
    print("Sorry, the number is not found")

else:
    print("the owner of the number is :", phone_book[phone_number])  
      


#Q2
#function that receives a list containing the following numbers
def move(list):
    zeroes = list.count(0)
    list = [i for i in list if i != 0]
    list += [0] * zeroes
    return list
list = [5, 0, 34, 9, 0, 13, 8]
new_list = move(list)
print(new_list)