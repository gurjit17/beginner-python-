# In this code we are covered the conditional statement in python 

# simple example how to work 
a = 26 
b = 108 
if b > a:
  print(' b is greater than a ') 

# if conditional statement 
age = 26 
if age > 19: 
  print('you are adult')

# if else conditional statement 
temperature  = 30
if temperature > 25: 
  print('it is hot today')
else : 
  print('it is cool day')
   
temperature  = 20
if temperature > 25: 
  print('it is hot today')
else : 
  print('it is cool day')

# if elif else conditional statement 
score = 86 
if score >=90:
  print('grade-a')
elif score >=80:
  print('grade-b')
elif score >=70: 
  print('grade_c')
else:
  print('grade-d')

score = 56 
if score >=90:
  print('grade-a')
elif score >=80:
  print('grade-b')
elif score >=70: 
  print('grade_c')
else:
  print('grade-d')

# Nested 'if else' conditinal statement 
number = 10 
if number > 0: 
  if number % 2 ==0: 
    print(' the number is positive and even. ')
else: 
  if number ==0: 
    print('the number is zero.')
  else: 
      print('the number is negative.')

number = -19
if number > 0: 
  if number % 2 ==0: 
    print(' the number is positive and even. ')
else: 
  if number ==0: 
    print('the number is zero.')
  else: 
      print('the number is negative.')

# conditional expressions 
age = 16 
status = 'adult' if age >=18 else 'Minor'
print(status)

age = 22 
status = 'adult' if age >=18 else 'Minor'
print(status)