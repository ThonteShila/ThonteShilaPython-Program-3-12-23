year=int(input("enter year"))
if year % 400 == 0:
    print("leap year")
elif year % 4 == 0:
    if  year % 100 == 0: 
        print("not a leap year")
    print("leap year")
print("not a leap year")