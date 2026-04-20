'''
    String in Python
    - Immutable in python
'''

word1 = "Hello "
word2 = "python"

#concatenate
print(word1+word2)

#len()
print(len(word2))

#string slicing [start:end) default: [start = 0, end = len(string_name)-1]
print(word2[2:5])

a = 5
b = 10
sum = a+b

#normal formatting using format()
print("language is {}".format("Python"))
print("sum of {} & {} is {}".format(a,b,sum))

#index based formatting usin format()
print("sum of {1} & {0} is {2}".format(a,b,sum))

#value based formatting 
print("values of vars {a} & {b}".format(a=9,b=10))


#formatting using f-string [modern way]
print(f"Sum of {a} and {b} is {sum}")
print(f"The avg of {a} and {b} is {(a+b)/2}")


'''
    List in Python
    - Mutable in python
'''

marks = [95,90,89,92,98]

print(marks[2])
print(len(marks))

marks[2] = 70
print(marks[2])

for i in range(0,len(marks)):
    print(marks[i],end=" ")
print()

print(marks[:])
print(marks[2:len(marks)])

'''
    List Methods
    - l.append(val) #add one element at the end
    - l.insert(idx,val) #insert element at idx
    - l.sort() #arranges in increasing order
    - l.reverse() #reverses order
'''

l = []
l.append(4)
l.append(5)
l.insert(2,10)
l.insert(0,12)
print(l[:])
l.sort()
print(l[:])
l.reverse()
print(l[:])

x = 5

for i in range(0,len(l)):
    if(l[i]==x):
        print(f"x found at index {i}")

'''
    Tuples in Python
    - Immutable in python
'''

tup = (1,2,3,"abc",3.14)

print(tup)
print(type(tup))

print(tup[:])

for i in range(0,len(tup)):
    print(tup[i],end=" ")
print()

'''
    Tuple Methods
    - t.index(val) #returns 1st occurence idx
    - t.cound(val) #counts total occurrences
'''

print(tup.index("abc"))
print(tup.count(3.14))


'''
    Dictonary in Python
    - Mutable in python
    - they are unordered
'''

dict = {
    "name":"Akhlaq Husain",
    "cgpa":9.94,
    "subjects":['computer science','maths','software engineering']
}

print(dict["name"])
print(dict["subjects"][0])

'''
    Dictonary Methods
    - d.keys() #returns all keys
    - d.values() #returns all values
    - d.items() #returns (key,value) pairs
    - d.get(val) #returns val acc. to key
    - d.update(new_item) #adds new item to dict
'''

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get('name'))
dict.update({'gender':'male'})
print(dict)

'''
    Set in Python
    - ordered
    - Mutable in python but the elements should be immutable
    - collection of unique values
'''

s = {1,2,3,2,3}

print(s)
print(type(s))

'''
    Set methods
    - s.add(val) #adds a val
    - s.remove(val) #removes a val
    - s.clear() #empties the set
    - s.pop() #removes a random val
    - s.union(set2) #returns new union
    - s.intersection(set2) #returns new intersection
'''

s.add(5)
print(s)
s.remove(1)
print(s)
s.clear()
print(s)
s.add(1)
s.add(5)
s.add(3)
print(s)
s.pop()
print(s)
s2 = {5,6,7,8,9}
print(s.union(s2))
print(s.intersection(s2))