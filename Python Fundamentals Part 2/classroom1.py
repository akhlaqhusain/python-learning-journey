'''
    Conditional Statements in Python
    - if
    - elif
    - else
'''

#---------------------------------------------------------------#
age = 19

if age>=18 :
    print("you can vote")
else:
    print("you can not vote")
#---------------------------------------------------------------#


#---------------------------------------------------------------#
traffic_light = 'green'

if traffic_light=='red':
    print('stop')
elif traffic_light=='green':
    print('go')
elif traffic_light=='yellow':
    print('look')
else:
    print('invalid light')
#---------------------------------------------------------------#


#---------------------------------------------------------------#
age = int(input('enter your age : '))

if age>=18:
    print('adult')
elif age>=13:
    print('teen')
else:
    print('child')
#---------------------------------------------------------------#


#---------------------------------------------------------------#
username = input('enter username: ')
password = input('enter password: ')

if (username=='admin' and password=='pass'):
    print("Access Granted!")
else:
    print('Access Declined!')
#---------------------------------------------------------------#


#---------------------------------------------------------------#
num = int(input('enter a number: '))

if num%2:
    print('odd')
else:
    print('even')
#---------------------------------------------------------------#

#---------------------------------------------------------------#
'''
    Match Case in Python
'''
color = 'yellow'

match color:
    case 'green':
        print('go')
    case 'red':
        print('stop')
    case 'yellow':
        print('look')
    case _:#default case written by underscore _ in python.
        print('wrong color')
#---------------------------------------------------------------#