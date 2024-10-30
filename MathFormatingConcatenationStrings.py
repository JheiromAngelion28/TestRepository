
# Doing Addition, Subtraction, Multiplication, Division, and Exponent.
a = 20
b = 10
sum = a + b 
print("The addition of", a, "and", b, "is",sum) 

a = 20
b = 10
sum = a - b 
print("The subtraction of", a, "and", b, "is",sum) 

a = 20
b = 10
sum = a * b 
print("The multiplication of", a, "and", b, "is",sum) 

a = 20
b = 10
sum = a // b 
print("The division of", a, "and", b, "is",sum) 


a = 20
b = 10
sum = a % b 
print("The remainder of", a, "and", b, "is",sum) 


a = 20
b = 10
sum = a ** b 
print("The  exponent of", a, "and", b, "is",sum) 

#String concatenation combines aother strings.

message = ('Hello ' + 'to ' + 'josh ' + 'Marshal ' + 'Tomas ' + 'Palico ' + 'Marcelino ' + 
           'A good day.')

# Formatting A certain string
print(f'Hello world')

#Printing a variable 
name = 'johnny'
print(f'Hello {name}.')

# f dose all the proccesing results and paste the result in format shape. This is all in the print statement.
print(f'The value is {10 + 2}.')

val = 10
print(f'The value is {val + 2}.')

num = 123.456789

#Formated to 2 decimal places 
print(f'{num:.2f}')

#Other examples of format strings

num = 1000000.00
print(f'{num:.2f}')

discount = 0.5
print(f'{discount:.0%}')


num = 123456789
print(f'{num:,d}')

num = 12345.6789
print(f'{num:.2e}')

# Specifying minimum field width
num = 12345.6789
print(f'The number is {num:12,.2f}')

#Alingning Values wnthin a field
print(f'{num:<20.2f}')
print(f'{num:>20.2f}')
print(f'{num:^20.2f}')


print(f'{24:^10,.2f}')



import turtle

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)


turtle.mainloop()




