# # import random 



# # list = ['king','queen', 'prince']



# # selectedValue = int(input('please select a number "0,1 or 2"'))

# # computerNumber = random.randint(0,2)

# # random.shuffle(list)

# # if list[selectedValue] is 'king':
    
# #     print('userwin')

# # elif list[selectedValue] is 'queen' and list [computerNumber] is 'king':
# #     print('your lost :(')
# # else:
# #     print('you lost')



# # import random 



# # number = [11,22,33,44,55,66,77,88,99]




# # selectedValue = int(input('please select a number "11,22,33,44,55,66,77,88,99"'))

# # computerNumber = random.randint(0,number)

# # random.shuffle(number)

# # if number[selectedValue] is '11,22,33,44,55,66,77,88,99':
    
# #     print('you win :(')

# # elif number[selectedValue] is '11' and number [computerNumber] is '11' :
# #     print('you win :(')

# # elif number[selectedValue] is '22' and number [computerNumber] is '22':
# #     print('you win :(') 
    

# # elif number[selectedValue] is '33' and number [computerNumber] is '33':
# #     print('you win :(')

# # elif number[selectedValue] is '44' and number [computerNumber] is '44':
# #     print('you win :(')

# # elif number[selectedValue] is '55' and number [computerNumber] is '55':
# #     print('you win :(')

# # elif number[selectedValue] is '66' and number [computerNumber] is '66':

# #     print('you win :(')

# # elif number[selectedValue] is '77' and number [computerNumber] is '77':
# #     print('you win :(')
# # else:
# #     print('you lost')




# import random

# def randomNumber(num):
#     num = int(num)
#     check = str(num)
#     randomNum = 23
#     rev = 0
#     while(num>0):
#         dig=num%10
#         rev=rev*10+dig
#         num=num//10
#     if len(check)>2:
#         print("please input two digit number")
#     else:
        
#         if num == randomNum:
#             print("You won 10000")

#         elif rev == randomNum:
#             print("You won 3000")
        
#         elif rev == randomNum:
#             print("You won 1000")
        

# randomNumber(input("Enter two digit number: "))

# import random
# randList, run = [], 0
# while run < 6:
#    number = random.randint(1,51)
#    if number not in randList:
#         if run == 5:
#             randList.append('+'+str(number))
#             break
#         randList.append(number)
#         run += 1
# print(randList)

import random
import time

##Declare Variables
user_num=0
##lottery_num=random.randint(10,99)
lottery_num=12

##Input
print("Welcome to the Lottery Program!")
user_num=int(input("Please enter a two digit number: "))
print("Calculating Results.")
for i in range(3):
  time.sleep(1)
  print(".")

##Calc & Output
lottery_tens = lottery_num // 10
lottery_ones = lottery_num % 10

user_tens = user_num // 10
user_ones = user_num % 10

if lottery_num == user_num:
    print("All your numbers match in exact order! Your reward is $10,000!\n")
elif lottery_tens == user_ones and lottery_ones == user_tens:
    print("All your numbers match! Your reward is $3,000!\n")
elif lottery_tens == user_tens or lottery_ones == user_ones \
  or lottery_ones == user_tens or lottery_tens == user_ones:
    print("One of your numbers match the lottery. Your reward is $1,000!\n")
else:
    print("Your numbers don't match! Sorry!")

##Same as Calc & Output using Sets.
##lottery_set = set('%02d' % lottery_num)
##user_set = set('%02d' % user_num)
##if lottery_num == user_num:
##    print("All your numbers match in exact order! Your reward is $10,000!\n")
##elif lottery_set == user_set:
##    print("All your numbers match! Your reward is $3,000!\n")
##elif lottery_set.intersection(user_set):
##    print("One of your numbers match the lottery. Your reward is $1,000!\n")
##else:
##    print("Your numbers don't match! Sorry!")