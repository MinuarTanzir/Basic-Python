attempts =0

nu = (range(100))

for i in nu:
    x= int(input("enter number"))
    if x ==55:
        print("you are right")
        break
    else:
        print("try again")
        attempts +=1
        if attempts == 3:
            print("Try next time")
            break
