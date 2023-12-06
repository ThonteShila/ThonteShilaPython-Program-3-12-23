num=int(input("no"))
def fact(num):
    if num == 1:
        return num
    else:
        return num*fact(num-1)
if num < 0:
    print("no not exist")
elif num == 1:
        print("fact is 1")
else:    
    print("factorial of no",fact(num))