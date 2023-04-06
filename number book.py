number_book={"Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"}

while True:
    user_input=input("Enter the phone number: ")
    if not user_input.isdigit()or len(user_input) !=10:
        print("This is an invalid number")
    else:
        found=False
        for name, phone in number_book.items():
            if phone == user_input:
                print(f"the owner of the number {user_input} is {name}")
                found=True
                break
            if not found:
                print(f"sorry the number {user_input} is not fund ")
        try_agen= input(" do you want try agen ?")
        if try_agen == "no":
            break