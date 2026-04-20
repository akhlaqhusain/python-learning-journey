'''
    Practice Problem
    - Given a list of tuples with info(name,subject):
        - List all unique courses
        - List students enrolled in English
        - Create dictonary (student,set of courses)
'''

info = [
    ('alice','math'),
    ('bob','science'),
    ('alice','science'),
    ('charlie','math'),
    ('bob','math'),
    ('alice','english'),
    ('charlie','english'),
]

unique_courses = set()
stud_enroll_in_eng = []
dict = {}

for d in info:
    unique_courses.add(d[1])
    if d[1]=='english':
        stud_enroll_in_eng.append(d[0])
    if(dict.get(d[0])==None):
        st = {d[1]}
        dict.update({d[0]:st})
    else:
        dict[d[0]].add(d[1])

print(unique_courses)
print(stud_enroll_in_eng[:])
print(dict)