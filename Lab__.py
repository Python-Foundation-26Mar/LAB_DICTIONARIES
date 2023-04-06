phone_book = {"0568323222" : "Amal", "0522222232" : "Mohammed", "0532335983" : "Khadijah"}

phone_number = input("What is the phone number? ")

if not phone_number.isdigit():
    print("This is invalid number, use only numbers.")
elif len(phone_number) < 10 or len(phone_number) > 10:
    print("This is invalid number")
elif not phone_number in phone_book:
    print("Sorry, the number is not found")
else:
    print("the owner of the number is: ", phone_book[phone_number])