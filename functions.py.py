#n=int(input())
n=2
for i in range(2,n//2+1):
    if n %i==0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")
    
#15 20  35
n1=15
for i in  range(2,n1//2+1):
    if n1 %i==0:
        print(f"{n1} is not a prime number")
        break
else:
    print(f"{n1} is a prime number")
n2=20
for i in  range(2,n2//2+1):
    if n2 %i==0:
        print(f"{n2} is not a prime number")
        break
else:
    print(f"{n2} is a prime number")
n3=35
for i in  range(2,n3//2+1):
    if n3 %i==0:
        print(f"{n3} is not a prime number")
        break
else:
    print(f"{n3} is a prime number")

#functions
#without parameters and without return
#function definition
def addition():
    a=10
    b=20
    print(a+b)
#funcion calling
#addition()
res=addition()
print(res)
# if function doesnt contain any return keyword ,it try to print result ,
#it will automatically returns none

#without parameters and with return
#function definition
def addition():
    a=10
    b=20
    return a+b
  
#funcion calling
res=addition()
print(res)

#with parameters and without return
#function definition
def addition(a,b):
    print(a+b)
#funcion calling
c=10
d=20
addition(c,d)
#res=addition(c,d)
#print(res)

#withparameters and with return
#function definition
def addition(a,b):
    print(a+b)
#funcion calling
#addition()
c=10
d=20
res=addition(c,d)
print(res)

#types of arguments

#positional arguments
#function definition
def division(a,b):
    if b==0:
        return "zero division not possible"
    return a/b
#function calling
c,d=10,5
res=division(c,d)
print(res)

#keyword arguments
#function definition
def division(a,b):
    if b==0:
        return "zero division not possible"
    return a/b
#function calling
c,d=10,5
res=division(b=d,a=c)
print(res)

#default arguments
#function definition
def addition(a,b,c=0,d=0):
    return a+b+c+d
#function calling

res1=addition(10,15)
res2=addition(10,15,-5)
res3=addition(10,15,10,10)
print(res1,res2,res3)

#Varaiable length arguments
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome',)

#keyword variable length arguments
def fun(**kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))

# Driver code
fun(s1='1', s2='2', s3='3')











































































    
    
















    
