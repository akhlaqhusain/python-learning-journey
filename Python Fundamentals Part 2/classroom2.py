'''
    While loop in Python
'''
#---------------------------------------------------------------#
cnt = 1
while cnt!=11:
    print(f"Akhlaq! {cnt}")
    cnt+=1
#---------------------------------------------------------------#
cnt = 5
while cnt > 0:
    print(cnt)
    cnt -= 1
#---------------------------------------------------------------#
n = int(input('enter number : '))
cnt = 1
while cnt < 11:
    print(f"{n} x {cnt} = {n*cnt}")
    cnt += 1
#---------------------------------------------------------------#
'''
    break and continue statements in python
'''
cnt = 1
while True:
    if cnt==10:
        break
    if cnt % 2 == 0:
        cnt += 1
        continue
    print(cnt)
    cnt+=1
#---------------------------------------------------------------#
'''
    For loop in python
    - in => membership operator, it is use to track value inside container and also use to check the presence of value inside the container.
    - range(n) => function that generates a sequence of numbers from [0,n-1].
    - range(1,n) => function that generates a sequence of numbers from [1,n-1].
    - range(starting_value,stop_value,step_value) => Here stop_value is compulsory.
'''
string = "hello"
for val in string:
    print(val)

if 'l' in string:
    print("l is present in the given string")
else:
    print("l is not present in the given string")

for i in range(5):
    print(i,end=' ')
print()
#---------------------------------------------------------------#
word = "artificial"
vowels = 0
for _ in word:
    if (_=='a' or _=='e' or _=='i' or _=='o' or _=='u'):
        vowels += 1
print(f"There is {vowels} vowels in the word {word}.")
#---------------------------------------------------------------#
for _ in range(1,10,2):
    print(_,end=' ')
print()
#---------------------------------------------------------------#
n = int(input('enter the value of n : '))
sum = 0
for i in range(1,n+1):
    sum += i
print(f'sum of first {n} natural number is : {sum}.')
#---------------------------------------------------------------#
