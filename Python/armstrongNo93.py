
num=int(input("Enter a number"))
temp=num
arm_no=0
while num > 0:
    rem=num%10
    arm_no=arm_no+rem*rem*rem
    num=num // 10
print(arm_no)

if temp == arm_no:
    print("this is arm_no",arm_no)
else:
    print("this not",arm_no)