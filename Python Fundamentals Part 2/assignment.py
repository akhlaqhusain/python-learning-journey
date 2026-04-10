#Q1 Answer

salary = float(input('enter your salary : '))
tax = 0

if salary > 70000:
    tax = salary * (0.25)
elif salary >= 30000:
    tax = salary * (0.15)
else:
    tax = salary * (0.05)
    
print(f'you have to pay {tax} amount as tax for having {salary} salary.')

#Q2 Answer

def ans(a,b):
    for i in range(a,b+1):
        if i % 2 == 0:
            print(i)
ans(2,20)

#Q3 Answer

def print_digits(n):
    while n>0:
        print(n%10,end=' ')
        n //= 10
    print()
print_digits(132)

#Q4 Answer

def count_of_digits(n):
    cnt = 0
    while n>0:
        cnt += 1
        n //= 10
    return cnt
print(count_of_digits(132))

#Q5 Answer

def sum_of_digits(n):
    sum = 0
    while n>0:
        sum += n%10
        n //= 10
    return sum
print(sum_of_digits(132))

#Q6 Answer

for i in range(1,1001):
    if i%3==0 and i%5==0:
        print(i,end=' ')
print()

#Q7 Answer

temp = 'hey'
while temp!='Quit':
    n = int(input('enter number : '))
    if n<0:
        print('negative')
    elif n==0:
        print('neigther negative nor positive')
    else:
        print('positive')
    temp = input('enter Quit to quit the program : ')

#Q8 Answer

def calculator(a,b,operator):
    match operator:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return a/b
        case _:
            return "Operator is not recognized by this function!"
print(calculator(5,4,'*'))

#Q9 Answer

def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(isPrime(7))
print(isPrime(21))
print(isPrime(0),isPrime(1),isPrime(101))

#Q10 Answer

target = 21
guess = 0
while guess!=target:
    guess = int(input('enter your guess : '))
    if guess > target:
        print('Too High')
    elif guess < target:
        print('Too Low')
    else:
        print('Correct!')