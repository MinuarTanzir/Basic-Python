# nums =[1,2,3,4,5,6,7,8,9,10,11,55]
#
# sum =0
#
# for num in nums:
#     if num % 2==1:
#         # print("odd number")
#         sum+=num
# print("Total of odd num", sum)
#
# if sum <50:
#     for i in range(10):
#         print("success")
# else:
#     print("success")

# nums =[1,2,3,4,5,6,7,8,9,10,11,55]
#
# sum =0
#
# for num in range(len(nums)):
#     print(nums[num])
#     if nums[num] % 2==1:
#         # print("odd number")
#         sum+=nums[num]
# print("Total of odd num", sum)
#
# if sum <50:
#     for i in range(10):
#         print("success")
# else:
#     print("success")

# nums =[1,2,3,4,5,6,7,8,9,10,11,55]
# max =  float("-inf")
# for i in nums:
#     max = i
# print(max)


nums =[1,2,3,4,5,6,7,8,9,10,11,55]

sum =0

for i in nums:
    if i % 2==1:
        # print("odd number")
        sum+=i
print("Total of odd num", sum)

if sum <50:
    for i in range(10):
        print("success")
else:
    print("success")