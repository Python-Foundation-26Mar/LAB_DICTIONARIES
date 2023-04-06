names = {"Amal":568323222,"Mohammed":522222232 , "Khadijah"	:532335983,
"Abdullah":545341144,"Rawan":545534556,"Faisal"	:560664566,"Layla":567917077}

print("a phone book program ")
value1=input("enter the  number ")


dic = int(value1)
if dic in names:
    print(names[dic])
elif dic not in names:
        print("Sorry, the number is not found")
elif len(str(dic)) > 10:
        print("This is invalid number")
elif len(str(dic)) < 10:
        print("This is invalid number")

else:
        print("This is invalid number")




# Sort  of the  numbers
numbers = [5, 0, 34, 9, 0, 13, 8]
print("Original: ",numbers)
sort_numbers = sorted(numbers)
print("Sorted:",sort_numbers)



n = len(numbers)
j = 0
for i in range(n):
    if numbers[i] != 0:
        numbers[j], numbers[i] = numbers[i], numbers[j]  
        j += 1
print(numbers)