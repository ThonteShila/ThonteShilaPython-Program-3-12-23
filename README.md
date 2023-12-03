# ThonteShilaPython-Program-3-12-23
This repository contains Python program while learning 
|| Jay Jay Raghuveer Samarth||
How Do I Know What Version of Python 
python --version

Gives Error
PS G:\Job Search shila 2023\Python Real staring from 3-12-23\ThonteShilaPython-Program-3-12-23> python --ver                 
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
setting -app and feature-app  Execution Aliases -Disable app installer (python)

To run program
1 py .\Hello.py

2 one line comment #
3 multiline comment """   """

4var Declaration:
5 carname="volvo"
6x=50
7x,y,z="fd","sf","sda"
8 x=y=z="fd"

9to make the variable x belong to the global scope.
10def myfunc():
 global x
 x = "fantastic"

11print the data type of x, what data type would that be
x = "Hello World"
print(type(x))
o/p=str

12 x = ["apple", "banana", "cherry"]
print(type(x))
o/p=list

13 x = ("apple", "banana", "cherry")
print(type(x))
o/p=tuple

14 x = {"name" : "John", "age" : 36}
print(type(x))
o/p=dict

15 x = {"name" : "John", "age" : 36}
print(type(x))

16 x=True
print(type(x))
o/p=bool

17 to convert x into a floating point number.
x = 5
x = float(x)

18 len function to print the length of the string.
x = "Hello World"
print(len(x))

19 first character of the string txt.
txt = "Hello World"
x = txt[0]

20 x = txt[2:5]   o/p=llo

21 to convert x into a complex.
x=5
x=complex(x)

22 to convert x into a integer.
x=5.4
x=int(x)

23 Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()

24Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()

25 Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H","J")

26 Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

27 print a Boolean value, 
print(10 > 9)
True

28
print(10 == 9)
False

29
print(10 < 9)
False

30
print(bool("abc"))
True

31
print(bool(0))
False

32 multiply 10 with 5, and print the result.
print(10*5)

33 Divide  10 with 5, and print the result.
print(10/5)

34 To check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

35 Use the correct comparison operator to check if 5 is not equal to 10.
if 5 != 10:
  print("5 and 10 is not equal")

36 Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

37Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

38 Change the value from "apple" to "kiwi", in the fruits list
fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"

39 Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
40 Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

41Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

42Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

43Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

44.Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))