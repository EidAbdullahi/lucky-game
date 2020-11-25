import random 



list = ['king','queen', 'prince']



selectedValue = int(input('please select a number "0,1 or 2"'))

computerNumber = random.randint(0,2)

random.shuffle(list)

if list[selectedValue] is 'king':
    
    print('userwin')

elif list[selectedValue] is 'queen' and list [computerNumber] is 'king':
    print('your lost :(')
else:
    print('you lost')



# import random 



# number = [1,2,3,4,5,6,7,8,9,10]



# selectedValue = int(input('please select a number "0,1,2,3,4,5,6,7,8,9,10'))


# computerNumber = random.randint(0,10)

# random.shuffle(number)

# if number[selectedValue] is '0,1,2,3,4,5,6,7,8,9,10':
    
#     print('userwin')

# elif number[selectedValue] is '2' and number [computerNumber] is '2':
#     print('you win :(')

# elif number[selectedValue] is '6' and number [computerNumber] is '6':
#     print('you win :(')

# elif number[selectedValue] is '8' and number [computerNumber] is '8':
#     print('you win :(')

# elif number[selectedValue] is '10' and number [computerNumber] is '10':
#     print('you win :(')
# else:
#     print('you lost')









