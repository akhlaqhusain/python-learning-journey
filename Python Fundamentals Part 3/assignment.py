#Q1 Answer

def check_palindrome(input_str):
    i,j = 0,len(input_str)-1
    while i<=j:
        if input_str[i]!=input_str[j]:
            return False
        i+=1
        j-=1
    return True

input_str = input("enter string : ")

if check_palindrome(input_str):
    print(f"{input_str} is a palindrome")
else:
    print(f"{input_str} is not a palindrome")

#Q2 Answer

ls = [1,2,3,4,5,2,4,5,9,100]

sum = 0
for i in ls:
    sum += i

print(f"Avg of all numbers in the given list is {sum/len(ls)}")

#Q3 Answer

ls1,ls2 = [5,3,6,2,1],[10,7,8,9]

for i in ls2:
    ls1.append(i)

ls1.sort()
print(ls1[:])

#Q4 Answer

tup = (1,2,3,4,5,6,7,8,9,10)

odd = []
eve = []

for i in tup:
    if i%2==0:
        eve.append(i)
    else:
        odd.append(i)

print(eve[:])
print(odd[:])

#Q5 Answer

dict = {}
while True:
    print('A: add a student\nB: update cgpa\nC: search for student\nD: display all students and their cgpa\nE: exit')
    val = input('enter your choice : ')
    val = val.upper()
    match val:
        case 'A':
            name = input("enter student's name : ")
            cgpa = input("enter student's cgpa : ")
            dict.update({name:cgpa})
            print('student added successfully')
        case 'B':
            name = input("enter student's name : ")
            cgpa = input("enter student's updated cgpa : ")
            dict[name] = cgpa
            print('student updated successfully')
        case 'C':
            name = input("enter student's name : ")
            if(dict.get(name)==None):
                print('student is not present in the database')
            else:
                print(f"Student's Name : {name}\nStudent's cgpa : {dict[name]}")
        case 'D':
            for i in dict:
                print(f"Student's Name : {i}\nStudent's cgpa : {dict[i]}")
        case 'E':
            print('exiting...')
            break
        case _:
            print('invalid choice')

#Q6 Answer

words = ['apple','banana','kiwi','cherry','mango']

ans = {}

for i in words:
    ans.update({i:len(i)})

print(ans)

#Q7 Answer

str = input('enter a string : ')
cnt = 0
for i in range(0,len(str)):
    if str[i] == ' ':
        cnt += 1
print(cnt)

#Q8 Answer

def check8(ls1,ls2):
    set1 = set(ls1)
    set2 = set(ls2)
    if set1.intersection(set2) == set():
        return True
    else:
        return False
    
print(check8([1,2,3],[3,4]))
print(check8([1,2],[3]))
    
#Q9 Answer

def check9(ls):
    st = set(ls)
    for it in st:
        if ls.count(it)>1:
            print(it)

check9([1,1,2,4,3,4])

#Q10 Answer

def check10(str):
    st = set(str)
    for it in st:
        print(f"{it} = {str.count(it)}",end='\t')

check10("akhlaqHusain")