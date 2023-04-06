#A 
phone_book = {
    'Amal': '0568323222',
    'Mohammed': '0522222232',
    'Khadijah': '0532335983',
    'Abdullah': '0545341144',
    'Rawan': '0545534556',
    'Faisal': '0560664566',
    'Layla': '0567917077'
}

def get_owner_by_number():
    phone_number = input("Enter the phone number: ")
    if not phone_number.isdigit() or len(phone_number) != 10:
        print("This is an invalid number.")
        return

    for name, number in phone_book.items():
        if number == phone_number:
            print("The owner of the number is:", name)
            return
    print("Sorry, the number is not found.")

get_owner_by_number()

#B

def rearrange_zeros(lst):
    zero_count = lst.count(0)
    lst = [elem for elem in lst if elem != 0]
    lst += [0] * zero_count
    return lst
lst = [5, 0, 34, 9, 0, 13, 8]
arranged_lst = rearrange_zeros(lst)
print(arranged_lst)
