# names=['kjs','shshs','shjy','hyw7uw','kiunj','jshswy','hjwyw']
# for name in names:
#     print(name)
#     print(name*3)

# name = 'kjhhs'
# for i in name:
#     print(i)

# name = ['kjhhs']
#
# for i in name:
#     print(i*10)
#
# #
# name = (input("Enter name"))
# i = 0
# while i <= 15 :
#     print("I am", name)
#     i = i+1
# print("end")

# name = (input("Enter name"))
# i = 0
# for i in range (1, 15):
#     print("I am", name)
#     i += 1
# print("end")

# name = (input("Enter name"))
# i = 0
# for i in range (1, 15):
#     if i <=10:
#         print("I am", name)
#     else:
#         name = (input("Enter name"))
#         print("I am not", name)
#     i += 1
# print("end")
#
# roll = int(input("Enter number"))
# i = 0
# len(6)
# for i in range (1, 20):
#     if i <=10:
#         print("Its under", roll)
#     else:
#         name = (input("Enter number"))
#         print("Its a not under", roll)
#     i == 1
# print("end")
#
# # Maximum number of attempts
# max_attempts = 3
#
# for attempts in range(max_attempts):
#     # Get the input from the user
#     roll_number = input("Enter the roll number: ")
#
#     # Check if the roll number is exactly 6 digits
#     if len(roll_number) == 6 and roll_number.isdigit():
#         print(f"Roll number {roll_number} found. We will show you the details.")
#         break
# else:
#     # This else block executes if the loop completes without a break
#     print("Timeout reached. Exiting program.")

# Initialize a counter for attempts
attempts = 0

while True:
    # Get the input from the user
    roll_number = input("Enter the roll number: ")

    # Check if the roll number is exactly 6 digits
    if len(roll_number) == 6 and roll_number.isdigit():
        print(f"Roll number {roll_number} found. We will show you the details.")
        break
    else:
        print("Invalid roll number. It must be exactly 6 digits.")
        attempts += 1
        # Check if attempts have reached 2
        if attempts >= 2:
            print("Timeout reached. Exiting program.")
            break
