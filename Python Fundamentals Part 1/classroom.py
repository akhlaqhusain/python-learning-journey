print("Hello World")
print("Hello \nI'm Akhlaq Husain","\nWho are you? ")

'''
    Variables in Python
    -> {syntax} => variable_name = data
'''

name = "Akhlaq Husain"
age = 19
PI = 3.14

print(name,age+2,PI)

'''
    Data Types in Python
    - Integers
    - Strings
    - Float 
    - Boolean
    - None
'''

isTrue = False
x = None

print(type(name),type(age),type(PI),type(isTrue),type(x),sep='\n')

'''
    Arithmetic Operators in Python
    -> +, addition
    -> -, subtraction
    -> *, multiplication
    -> /, division
    -> //, for floor division
    -> %, modulo operator
    -> **, power operator 2**3 = 8
'''

a = 10
b = 5

print(a+b) #prints 15
print(a-b) #prints 5
print(a*b) #prints 50
print(a/b) #prints 2.0
print(a//b) #prints 2
print(a%b) #prints 0
print(a**b) #prints 100000

'''
    Relational/Comparison Operators in Python
    -> <, less than
    -> >, greater than
    -> ==, equal to 
    -> !=, not equal to 
    -> <=, less than and equal to
    -> >=, greater than and equal to
    Every operator returns either True or False
'''

#Here a = 10 and b = 5
print(a<b) # prints False 
print(a>b) # prints True
print(a==b) # prints False
print(a!=b) # prints True
print(a<=b) # prints False
print(a>=b) # prints True

'''
    Assignment Operator
    -> =, assigns value b to a -> a = b
    -> +=, a += b => a = a+b
    -> -=, a -= b => a = a-b
    -> *=, a *= b => a = a*b
    -> /=, a /= b => a = a/b
    -> %=, a %= b => a = a%b
    -> //=, a //= b => a = a//b
    -> **=, a **= b => a = a**b
'''

#Here initially a = 10 and b = 5
a += 2 # a = 10 + 2 = 12
a -= 4 # a = 12 - 4 = 8
a *= 3 # a = 8 * 3 = 24
a //= b # a = 24 // 5 = 4(floor value)
a **= 2 # a = 4 ** 2 = 16
print(a) #outputs 16

'''
    Logical Operator
    -> not
    -> and
    -> or
'''

var = False

print(not var) #outputs True
print(True and var) #outputs False
print(True or var) #outputs True

'''
    Operator Precedence {same precedence -> [left to right execution]}
    -> ()
    -> **
    -> *, /, %
    -> +, -
    -> ==, !=, >, >=, <, <=
    -> not
    -> and
    -> or
'''

'''
      Type Conversion in python
                |
      ------------------------
      |                      |
    Type                    Type
    Conversion              Casting (explicit
    (implicit               done by developers)
    done by python          e.g., x = int(4.5) #stores 4
    interpreter)
'''

print(type(5 + 10.0)) #Implicit type casting
print(type(int(5 + 10.0))) #Explicit type casting

'''
    Taking inputs from user in Python
    -- we can use input() function to take any input from user and the input is always considerd as a string, so if you are taking a integer value so do not forget to type cast the data as integer.
'''

username = input("Enter your name : ")
print("Hi",username)

x = input("Enter first value : ")
y = input("Enter second value : ")
print(x+y) #if x = 5 and y = 6 then outputs 56 which is wrong because the input data is stored as a string and the result will be the concatenation of x and y, so we have to convert the data to integer first.

x = int(input("Enter first value : "))
y = int(input("Enter second value : "))
print(x+y) #Now the output is x+y the sum of x and y.

# WAP to print the average of two numbers

x = int(input("Enter first value : "))
y = int(input("Enter second value : "))

avg = (x+y)/2

print(f"The average of {x} and {y} is {avg}.") #This is done using format string