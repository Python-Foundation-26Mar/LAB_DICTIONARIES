## Q1:Build a phone book program that receives the phone number 
#(Use Input to let the user provide the number), and returns the name of the owner. 


x={'Amal':568323222,'Mohammed':522222232,'Khadijah':532335983,'Abdullah':545341144,'Rawan':545534556,'Faisal':560664566,'Layla':567917077}
for key in x.values():
    key=int(input("Enter number here:"))
    print(key)
    if key == x:
        key=x.keys()
        print(x)
        continue
    elif key<10 and key>10 :
        print("This is invalid numberr")
    else:
        print("This is invalid number")
x.get()


# Q2:Write a function that receives a list containing the following numbers : 


number_list=[5,0,34,9,0,13,8]
number_list.sort(reverse=True)
print(number_list)
number_list.sort()
print(number_list)

