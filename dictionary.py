phone_number_book = {"0568323222" : "Amal", "0545534556" : "Rawan", "0560664566" : "Faisal"}
phone_number_book = input ("what is the phone number? ")

if not phone_number_book.isdigit():
    print("This is invalid number, use only numbers.")
elif len (phone_number_book) <10 or len (phone_number_book) >10:
    print("This is invalid number")     
elif not phone_number_book in phone_number_book:
    print ("Sorry, the number is not found")
else:
    print("the owner of the number is: ", phone_number_book [phone_number_book])    