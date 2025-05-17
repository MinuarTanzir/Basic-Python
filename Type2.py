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

#16.break and continue
#16.1.break-basic
i=1
while i<=50:
    print(i)
    i = i + 1
    if i==45:
        break
#16.2.break-advance
i=1
n=int(input("Number"))
while i<=n:
    print(i)
    i = i + 1
    if i==45:
        break

#16.3.continue
i=1
n=int(input("Number"))
while i<=n:
    print(i)
    i = i + 1
    if i==45:
        continue
print("Finish")
## output will change if " continue " statement move forward
i=1
n=int(input("Number"))
while i<=n:
    if i==45:
        continue
    print(i)
    i = i + 1
print("Finish")

#17.List

subject= ["math","bangla","english","python"]
print(subject)
print(subject[2])
print(subject[2:])
print(subject[-1])
print("python" in subject)  # output true/false
print("Java" not in subject)  # output true/false

#17.1.

sub =["python","math","bangla","java","c#"]
sub.append("English")
print(len(sub))
print(sub)
sub.insert(3,"kotlin")
print(sub)
sub.remove("math")   #remove a particular portion
print(sub)
sub.sort()  # a-z order
print(sub)
sub.reverse()  #reverse the normal order
print(sub)
sub.pop()  #remove the last one
print(sub)
sub2 = sub.copy()
print(sub2)
dal=sub.index("c#")
print(dal)
sub.clear()
print(sub)

#18. Range function

num= list(range(15))
print(num)
num= list(range(15, 34))
print(num)
num= list(range(2,111,2))
print(num)