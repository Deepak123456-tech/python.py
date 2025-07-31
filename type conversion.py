
# integert to float , and string conversion 
num = 24
print(float(num))
print(str(num))

# integert to float , and string conversion 
num = 24
float_num = float(num)
print(type(float_num))
print(float_num)

# Float to integet and string conversion
num = 24.0
print(int(num))
print(str(num))

# string to integet, list, tuple , set
s1 = '123'
s2 = 'abc123ab'
print(int(s1))
print(list(s2))
print(tuple(s2))
print(set(s2))

# list to string, set, tuple
lst = [1,2,'a', 'Codegnan']
print(str(lst))
print(set(lst))
print(tuple(lst))

lst = [1,2,'a', 'Codegnan']
print(dict(lst))



## list of tuples to dictionary
l = [('a',1), ('b',2),('c',3)]
print(dict(l))
{'a': 1, 'b': 2, 'c': 3}
# set to string, list, tuple
s = {1,2,3,'a','Codegnan'}
print(list(s))
print(tuple(s))
[1, 2, 3, 'a', 'Codegnan']
(1, 2, 3, 'a', 'Codegnan')
# tuple to list, set 
t = (1,2,3,'hi')
print(list(t))
print(set(t))
[1, 2, 3, 'hi']
{1, 2, 3, 'hi'}
problem solving Game
Write a Python program to convert kilometers to miles?
Write a Python program to convert Celsius to Fahrenheit?
Write a Python program to display calendar?
Write a Python program to solve quadratic equation?
Write a Python program to swap two variables without temp variable?
# Write a Python program to convert kilometers to miles?
km = int(input())
miles = km / 1.609
print(miles)

# Write a Python program to convert Celsius to Fahrenheit?
celsius = int(input())
fahrenheit = celsius * 9/5 + 32
print(str(fahrenheit)  + ' F')

# Write a Python program to convert Fahrenheit to Celsius?
fahrenheit = float(input())
Celsius = (fahrenheit-32) * 5/9 
print(Celsius)

# Write a Python program to solve quadratic equation?
a,b, c = map(int, input().split())
numarator = ((b**2) - (4*a*c))**0.5
denomi = 2*a
root1 = (-b + numarator)/(denomi)
root2 = (-b - numarator)/(denomi)
print(root1, root2)

s = '1x^2 + 4x + 12'
l = s.split('+')
print(str(l[0])[:-4])
a, b, c = str(l[0])[:-4], str(l[1])[:-2], l[2]
print(a,b,c)

import calendar
#print(calendar.calendar(int(input())))
print(calendar.month(2025,7))




