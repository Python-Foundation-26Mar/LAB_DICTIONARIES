
    
list=[5, 0, 34, 9, 0, 13, 8]
count = 0
for i in range(len(list)):
    if list[i] != 0:
        list[i], list[count] = list[count], list[i]
        count += 1
print(list)
