start_number = int(input("E: "))
End_number = int(input("F: "))

i = start_number

if start_number < End_number:
    while i < End_number:
        if i % 3 == 0:  
            print(i)
        i += 2 
elif start_number > End_number:
    while i>End_number:
        if i % 3 == 0:  
            print(i)
        i -= 2  

else:
    print("E=F")
