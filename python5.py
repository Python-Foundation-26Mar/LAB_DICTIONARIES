phone_book = {
    'Amal': '0568323222',
    'Mohammed': '0522222232',
    'Khadijah': '0532335983',
    'Abdullah': '0545341144',
    'Rawan': '0545534556',
    'Faisal': '0560664566',
    'Layla': '0567917077'
}

phone_number = input("Enter the phone number: ")


if not phone_number.isdigit() or len(phone_number) != 10:
    print("This is invalid number")
else:
    owner = None
    for name, number in phone_book.items():
        if number == phone_number:
            owner = name
            break

    if owner is not None:
        print(f"The owner of the phone number {phone_number} is {owner}")
    else:
        print("Sorry, the number is not found")
def rearrange_zeros(lst):
    zero_count = lst.count(0)
    lst = [n for n in lst if n != 0] + [0] * zero_count
    return lst
lst = [5, 0, 34, 9, 0, 13, 8]
new_lst = rearrange_zeros(lst)
print(new_lst)
