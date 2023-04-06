''' phone book program that receives the phone number (Use Input to let the user provide the number), 
and returns the name of the owner.'''
#Q1
phone_book = (('Amal', '0568323222'), ('Mohammed', '0522222232'), ('Khadijah	', '0532335983'),
             ('Abdullah', '0545341144'), ('Rawan', '0545534556'), ('Faisal	', '0560664566',('Layla', '0567917077')))
def find_owner(phone_number):
    if not phone_number.isdigit() or len(phone_number) != 10:
        print("This is invalid number")
        return
    for name, number in phone_book:
        if number == phone_number:
            print(name)
            return
    print("Sorry, the number is not found")

phone_number = input("Enter a phone number: ")
find_owner(phone_number)

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