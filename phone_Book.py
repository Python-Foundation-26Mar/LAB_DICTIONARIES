my_Dictonary={"0568323222":"Amal","0522222232":"Mohammed","0532335983":"Khadijah","0545341144":"Abdullah","0545534556":"Rawan","0560664566":"Faisal","0567917077":"Layla"}
num=input("enter number:")

if not num.isdigit or num.__len__ !=10:
    print("This is invalid number")

elif not num in my_Dictonary:
    print ("the number is not found")
else:
    print("the owner of the number is: ", my_Dictonary.get(num))  


