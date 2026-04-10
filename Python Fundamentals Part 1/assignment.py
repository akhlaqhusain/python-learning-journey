#Q1 Answer

name = input("Enter your name : ")
age = int(input("Enter your age : "))

print(f"Hi {name}, you are {age} years old!")


#Q2 Answer

x = int(input("enter first number : "))
y = int(input("enter second number : "))

print(f"sum = {x+y}\ndifference = {x-y}\nproduct = {x*y}\nquotient = {x//y}")

#Q3 Answer

x = int(input("enter first integer value : "))
y = int(input("enter second integer value : "))
z = float(input("enter a float value : "))

avg = (float(x)+float(y)+z)/3

print(f"The average of all three numbers are : {avg}")


#Q4 Answer

x = input("enter a value : ")

x_int = int(x)
x_float = float(x)
x_string = str(x)

print(x_int,type(x_int))
print(x_float,type(x_float))
print(x_string,type(x_string))

# Q5 Answer

x = 10 + 3 * 2 ** 2 #output should be 22
#The precedence of power op is greater than product and addition op so 2**2 operation will execute first then after this the product op has more precedence than addition so 3 * 4 will execute and finally 10 + 12 = 22.
print(x)

#Q6 Answer

x = int(input("enter first value: "))
y = int(input("enter second value: "))

print(f"Initial values\nx = {x}, y = {y}.")
z = x
x = y
y = z
print(f"After swapping\nx = {x},y = {y}.")

#Q7 Answer

temp_in_cel = float(input("enter temperature in celcius : "))
temp_in_fahrenheit = (temp_in_cel*(9/5)+32)

print(f"{temp_in_cel} Celcius = {temp_in_fahrenheit} Fahrenheit.")

#Q8 Answer

r = float(input("enter the radius: "))
print(f"The area is {3.14*r*r}")

#Q9 Answer

p = float(input("enter principal : "))
r = float(input("enter rate : "))
t = float(input("enter time : "))

simple_interest = (p*r*t) / 100

print(f"Simple Interest = {simple_interest}")

#Q10 Answer

x = float(input("enter a decimal number : "))

x_int = int(x)
x_frac = x - x_int # or we can also do x % 1 for fractional part

print(f"Integer Part = {x_int}\nFractional Part = {x_frac}")