# 1.I am a noob
print(1.2)
print("Tanzir")

#2.Backslash
print("Tanzir \n 01722253037")
print("Tanzir\tis\tnot available")

#3.variables & Data types
name="Tanzir"
age =23.5
print("I am " + name)
print("I'm" ,age,'years old')
print("I have complete my bachelors")
print("Now\t"+name+"\tis doing nothing")

#4.Numerical Operation
a=15
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#5.user input
#5.1.basic(ui)
name="Tanzir"
age="24"
cgpa="3.13"
print("student info")
print(".................")
print("NAME: "+name)
print("AGE: "+age)
print("CGPA: "+cgpa)

#5.2.Advance(ui)
name=input("Enter Name:")
age=input("Enter Age:")
cgpa=input("Enter Cgpa:")
print("student info")
print(".................")
print("NAME: "+name)
print("AGE: "+age)
print("CGPA: "+cgpa)

#6.Type Casting
#6.1basic
num1 = input ("enter first number: ")
num2 = input ("enter second number: ")

sum= int(num1) + int(num2)
print("Total sum",sum)
diff= int(num1) - int(num2)
print("Total difference",diff)

#6.2Advance
num1 = int(input ("enter first number: "))
num2 = int(input ("enter second number: "))

sum= (num1) + (num2)
print("Total sum",sum)
sum= (num1) - (num2)
print("Total diff",sum)

#7.calculate area of plane shape
#7.1.for triangle
base =float(input("Enter Base ="))
height =float(input("Enter height ="))
area =.5 * base * height
print("area",area)

#7.2.for circle
radius =float(input("Enter radius ="))
area =3.1416 * radius * radius
print("area",area)

#8.library function
from math import*
#8.1.casual
value1 = min(10,20,30,40,60)
value2 = max(10,20,30,40,60)
print(value1 , value2)

#8.2.direct
print (min(10,20,30,40,60))
print (max(10,20,30,40,60))
print (abs(-10))
print (pow(10,2))
print (sqrt(9,))
print (round(10.51))
print (floor(10.99))
print (ceil(10.01))

#9.Type functions

value1 =10
value2 =10.10
value3 ="Tanzir"
print(type(value1))
print(type(value2))
print(type(value3))
print(type(True))
#9.1.sum
num1 =5
num2 =21
print("sum is ",num1+num2)
print("sum is" ,f"{num1}+{num2} = {num1+num2}")

#9.2.cancel new line
print("Tanzir", end=" ")
print("He is 24")

#10.Relational Operator & Boolean Data Type
print(20>=20)
print(20<=20)
print(20>20)
print(20<20)
print(20==20)
print(20!=20)

#10.1.if else statement

Total_marks =100
marks= 40
if marks>=50:
    print("pass")
    print("Congrats")
else:
    print("Fail")
    print("You are a disgrace")
print("Program ends here")

#10.2.largast number
num1=50
num2=-100
if num1>num2:
    print(num1)
else:
    print(num2)

#10.3.even/odd basic
num=10
if num%2==0:
    print("even")
else:
    print("odd")

#10.4.even/odd advance
num=int(input("Enter the number"))
if num%2==0:
    print("even")
else:
    print("odd")
print("Program Finished")

#10.5.elif statement

marks=78
if marks>=80:
    print("A+")
elif marks>=70:
    print("B+")
elif marks>=60:
    print("C+")
elif marks>=50:
    print("D+")
elif marks>=40:
    print("D")
elif marks>=33:
    print("D-")
else:
    print("Fail")

marks = int(input("Enter the number"))

print("This is your result")
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("C+")
elif marks >= 50:
    print("D+")
elif marks >= 40:
    print("D")
elif marks >= 33:
    print("D-")
else:
    print("Fail")

# practice with faris
password =str(input("Enter password"))
confirm_password =str(input("Enter password"))

if password==confirm_password:
    print("Password Correct")
else:
    print("Failed")

#11.Inner If Statement
if 7>=7:
    if 7>5:
        if 7>8:
            print("Yoh")
        else:
            print("Fuck")
#11.1.find the largest number

num1=125
num2=99
num3=411
if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num1:
        if num2>num3:
            print(num2)
        else:
            print(num3)

#12.Ternary Operator
num1=10
num2=200
print(num1 if num1>num2 else num2)
# or
max = num1 if num1>num2 else num2
print(max)

#13.Logical operator
#13.1.print highest
num1=25
num2=65
num3=90
if num1 > num2 and num1 > num3:
    print("num1=",num1)
elif num2 > num3 and num2 > num1:
    print("num2=",num2)
else:
    print("num3=",num3)
#13.2.print lowest
num1=25
num2=65
num3=90
if num1 < num2 and num1 < num3:
    print("num1=",num1)
elif num2 < num3 and num2 < num1:
    print("num2=",num2)
else:
    print("num3=",num3)
ch = input("Enter Character")
if ch == "a" or ch == "e" or ch =="i" or ch == "o" or ch == "u" :
    print("vowel")
else:
    print("consonent")

#14.while loop
i=2
while i<=25:
    print(i)
    i = i + 2
print("End")

#15some of n number
#15.1.basic
sum = 0
i =1
while i<=500:
    sum= (sum+ i)
    i= i+1
print (sum)
#15.2.advance
n=int(input("Enter number"))
sum = 0
i =1
while i<=n:
    sum= (sum+ i)
    i= i+1
print (sum)