#string concation using +
s1='srinu'
s2='babu'
print(s1+s2)

#string repetition using '*'
s='codegnan'
print(s*3)

##case conversion
s="I am from IndiA"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

##remove white spaces
s='  abc  '
print(s)
print(s.strip())
print(s.lstrip)
print(s.rstrip)

#find(),index()
s='I am a python programmer'
print(s.find('a'))
print(s.find('k'))
print(s.index('a'))
#print(s.index('k'))

#replace()
s='I am a python programmer'
print(s.replace('python','java'))

#split()
s='I am a python programmer'
print(s.split())

#join()
s=['I', 'am', 'a', 'python', 'programmer']
print("".join(s))


#checking
s1='abcd'
s2='abcd1234'
s3='1234'
print(s1.isalpha())
print(s2.isalnum())
print(s3.isdigit())

#srting comparision
s1='abcd'
s2='abde'
print(s1>s2)
print(s1<s2)

#the end







