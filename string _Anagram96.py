
str1=input("enter 1 st string")
str2=input("enter 2 st string")
list1=list(str1)
list2=list(str2)
print(list1)
print(list2)
list1.sort()
list2.sort()
print(list1)
print(list2)

def param(str1,str2):
    pos=0
    matches=True
    while pos < len(str1) and matches:
        if list1[pos] == list2[pos]:
            pos=pos+1
        else:
            matches=False
    return matches

print("strings are  anagram",param(str1,str2))
