# Yijie Zhang 1098690 Edward & Yifan Shen 1098328 Sivan
# Question 1
num = int(input("Enter a number: "))
while num <= 0:
    num = int(input("please input a new integer which is positive"))

# Question 2
if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
    print('The number', num, 'is multiple of l2,3,4')
else:
    print('The number', num, 'is not a multiple of 2,3,4')
print('End Of Program')
