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

45.Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

46.Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

47.Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

48.Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

49.Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

50Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

51Change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]=2020

52Add the key/value pair "color" : "red" to the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"

53 Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

54Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

55 print "Hello World" if a is greater than b.
a = 50
b = 10
if a > b:
  print("Hello World")


56 print "Hello World" if a is greater than b.
a = 50
b = 10
if a != b:
  print("Hello World")

57Print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10
if a == b:
  print("yes")
else:
  print("no")

58.Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a == b:
  print("1")
elif a>b:
  print("2")
else:
print("3")

59Print "Hello" if a is equal to b, and c is equal to d.
if a==b and c==d:
  print("hello")
  
60Print "Hello" if a is equal to b, or if c is equal to d.
if a==b or c==d:
  print("hello")

61Complete the code block, print "YES" if 5 is larger than 2.
if 5>2:
print("YES")

62Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").
a=3
b=6
print("yes") if a == b else   print("no")

63 Use an if statement to print "YES" if either a or b is equal to c.
a=2
b=3
c=5
if a == c or b == c:
  print("yes")

64 Print i as long as i is less than 6.
i=1
while i < 6:
  print("i")
  i +=1

65Stop the loop if i is 3.
i=1
while i < 6:
  if i == 3:
    break
  i +=1

66In the loop, when i is 3, jump directly to the next iteration.
i=1
while i < 6:
  if i == 3:
    continue
  i +=1
  print(i)

67Print a message once the condition is false.
i=1
while i < 6:
  print(i)
  i +=1
  else:
  print("condition false")
68. Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
69. In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

70. Use the range function to loop through a code set 6 times.
for i in range(6):
  print(i)

71. Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

72. Create a function named my_function.
def my_function():
  print("hi")

73. Execute a function named my_function.
def my_function():
  print("hi")
my_function()

74.Inside a function with two parameters, print the first parameter.
def my_function(x,y):
  print(x)

75.Let the function return the x parameter + 5.
def my_function(x):
  return x+5

76. If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(*kid):
  print("no of kis"+kid[2])

77. If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(**kid):
  print("His last name is " + kid["lname"])

78. Create a lambda function that takes one parameter (a) and returns it.
x =lambda a : a

79. Create a class named MyClass:
class MyClass:
  x=5

80. Create an object of MyClass called p1:
class MyClass:
  x=5
p1=MyClass()

81. Use the p1 object to print the value of x:
class MyClass:
  x=5
p1=MyClass()
print(p1.x)

82. What is the correct syntax to assign a "init" function to a class?
class MyClass:
  def __init__(self,x,y):
    self.x=x
    self.y=y

83. What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
class student(person):

84. We have used the Student class to create an object named x.
What is the correct syntax to execute the printname method of the object x?
class person:
  def __init__(self,fname):
    self.fname=fiestname
  def printname(self):
    print(self.firstname)
class Student(person):
  pass
x=Student("shila")
x.printname()

85. What is the correct syntax to import a module named "mymodule"?
import mymodule

86. If you want to refer to a module by using a different name, you can create an alias.
What is the correct syntax for creating an alias for a module?
import mymodule as mx

87. What is the correct syntax of printing all variables and function names of the "mymodule" module?
print(dir(mymodule))

88What is the correct syntax of importing only the person1 dictionary of the "mymodule" module?
from mymodule import person1

89. Adding two no
num1=20
num2=30
sum=num1+num2
print("Addition of two numbers is",sum)

90. Even Odd Program in Python
num=int(input("Enter a number to check odd or even"))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

91. Reverse a Number  /////Slicing method
num=int(input("Enter a number to check odd or even"))
n=str(num)
res=int(n[::-1])
print(res)

or

num=int(input("Enter a number"))
rev_no=0
while num > 0:
    rem=num%10
    rev_no=rev_no*10+rem
    num=num // 10
print(rev_no)

92. Armstrong number checking.
Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

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
    print("this is not arm_no",arm_no)

93. Check Leap year
import calendar
year=int(input("enter year"))
if calendar.isleap(year):
    print("leap year")
else: 
    print("not a leap year")
  
    or

    
year=int(input("enter year"))
if year % 400 == 0:
    print("leap year")
elif year % 4 == 0:
    if  year % 100 == 0: 
        print("not a leap year")
    print("leap year")
print("not a leap year")

94. Convert Celcius to Fahreinheit
Fahrenheit = (1.8 * celsius) + 32;

cel=int(input("enter temperature in celcious"))
fohreinheit=(cel*1.8) + 32
print("fohreinheit",fohreinheit)

95. Factorial of a Number
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


96. Anagram Program in Python
 if the second string is simply a rearrangement of the first, it is said to be an anagram of the first.

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

97.. Fizzbuzz Program
For numbers divisible by 3, it prints "Fizz" instead of the number.
For numbers divisible by 5, it prints "Buzz" instead of the number.
For numbers divisible by both 3 and 5, it prints "FizzBuzz" instead of the number.
n=int(input("enter how many number to print"))
for i in range(1,n+1):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i) 
  
98. Prime no
a number that is divisible only by 1 and itself.
num= int(input("enter no"))
flag=0
if num == 1:
    flag=1
    print("not Prime")
for i in range(2,num):
    if num % i == 0:
        print("Not prime ")
        flag=1
        break

if flag == 0:
    print("prime number")

99.