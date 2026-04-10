'''
    Functions in python
    - functions are block of statements that perform a specific task.
    - it is created by 'def' keyword
    - there is two parts of functions
        1. function definition 
        2. function call
    Functions is of two types:
    1. Built in functions ->> print(),range(),type(),input(),etc.
    2. User defined functions ->> sum(),greet(),etc.
'''
#---------------------------------------------------------------#
def greet(name):
    print(f"Hello {str.upper(name)}")

greet("akhlaq")
#---------------------------------------------------------------#
#function definition
def sum(a,b):#function parameters
    return a+b

res = sum(1,2)#function call
print(res)
#---------------------------------------------------------------#
def calc_avg(a,b,c):
    return (a+b+c)/3
print(calc_avg(3,5,19))
#---------------------------------------------------------------#
def rec(n,i=1):#here i is default parameter
    if i>n:
        return
    print(i)
    rec(n,i+1)
rec(5) #function call without i's value because i is default parameter
#---------------------------------------------------------------#
'''
    Lambda Functions
    - lambda functions are small anonymous functions that is defined by lambda keyword
    - {syntax} -> lambda para-1,para-2,..,para-N : expression
'''
sum = lambda a,b : a+b
print(sum(3,5))

avg = lambda a,b : (a+b)/2
print(avg(3,4))
#---------------------------------------------------------------#
#WAP to find the factorial of N using functions

def fact(n):
    res = 1
    for _ in range(1,n+1):
        res *= _
    return res

print(fact(5))
#---------------------------------------------------------------#