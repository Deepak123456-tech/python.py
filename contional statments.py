
# Write a program to check whether a number is positive or negative.
num = int(input())
if num >= 0:
    print(f'{num} is positive')
else:
    print(f'{num} is Negitive')

# Check whether a number is even or odd.
num = int(input())
if num%2 == 0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')

#Find the greater of two numbers.
n1, n2 = map(int, input().split())
if n1 > n2:
    print(f"{n1} is big")
else:
    print(f"{n2} is big")

# Find the largest among three numbers
a,b,c = map(int,input().split())
if a>b and a > c:
    print(f"{a} is big")
elif b > a and b > c:
    print(f"{b} is big")
else:
    print(f"{c} is big")

# Check if a number is divisible by 5 and 11.
num = int(input())
if num % 5==0 and num % 11 ==0:
    print(f'{num} is divisiable by 5 and 11')
else:
    print(f'{num} is not divisiable by 5 and 11')

# Check if a year is a leap year.
year = int(input())
if (year % 4 ==0 and year % 100 !=0) or year % 400 == 0:
    print(f'{year} is leap year')
else:
    print(f'{year} is not leap year')

# Check whether a character is a vowel or a consonant.
v = {'a','e','i','o','u','A','E','I','O','U'}
char = input()
if char in v:
    print(f"{char} is Vowel")
else:
    print(f"{char} is consonat")

# Check whether a number is a multiple of 3 or 7.
num = int(input())
if num % 3 == 0 or num % 7 ==0:
    print(f'{num} is a multiple of 3 or 7')
else:
    print(f'{num} is a not multiple of 3 or 7')

# Check whether a character is uppercase, lowercase, digit, or special symbol
char = input()
if char.islower():
    print(f'{char} is lower')
elif char.isupper():
    print(f'{char} is upper')
elif char.isdigit():
    print(f'{char} is digit')
else:
    print(f'{char} is special symbol')


 
