# in this code we are covered the how to input function can collect the data from the user 

# input fucntion in python

name = input('enter your good name:')
print('hello' + name + '!')
age  = input('enter yor age :')
print("i expected this age according your face..." + age +'!')

 #input fuction add 2 number 
 #from user to collect the first ans second number 

num_1 = input('enter the first number: ')
num_2 = input('enter the second number: ')

#since input returns the string , we need to convert it to an integer 
num_1 = int(num_1)
num_2 = int(num_2)

#calculate the sum and display the result 
sum = num_1 + num_2 
print('the sum of' , num_1 , 'and', num_2, 'is:',sum)

num_3 = input('enter your fvrt number: ')
num_4 = input('enter your fvrt second number: ')
num_3 = float(num_3)
num_4 = float(num_4)
sum = num_3 + num_4 
print("the sum of" , num_3 , 'and' , num_4, 'is', sum )

# input from the user and add the two numbers
x = input('enter the first number: ')
y = input('enter the second number : ')
print(f'sum of{x} & {y} is {int(x) + int(y)}')
