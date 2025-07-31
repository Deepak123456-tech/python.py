#tuple example
#t=(1,2,'a','codegynan',5.5,[1,23,45],10)

#initilize empty tuple
#t=()

#multiple values tuple
#t=(1,2,'a',4.5)

#single value tuple
#t=(34)

#indexing and slicable
t1=(1,2,'a','codegyan',5.5,2,1,[1,23,45],10)
print(t1[4])
print(t1[-4])
print(t1[-4:-1])
print(t1[-3:2:1])
print(t1[-3:2:-1])
print(t1[5:100:1])

#tuple reading from user
#t=input()
#t2=tuple(map(int,t.split()))
#print(t2)

#tuple concatination using '+'
t3=(1,2,'hi')
t4=(3,4,'bye')
t5=t3+t4
print(t5)

#tuple repeat using '*'
t6=(1,2,'hi')
print(t6*4)

#tuple methods
#count(value),index()
t7=(1,2,'a','codegynan',5.5,2,1,[1,23,34],10)
count_1=t7.count(1)
print(count_1)
index=t7.index([1,23,34])
print(index)


#bulit in functions
#min(),max(),sum(),len()
t=[1,2,20,50,30,60]
min_value=min(t)
max_value=max(t)
sum_tuple=sum(t)
length=len(t)
print(min_value)
print(max_value)
print(sum_tuple)
print(length)


#sorted() not sort
t8=(1,2,20,50,30,60)
t9=sorted(t8)
print(t9)

#membership operators
t10=(1,2,20,40,50)
print(2 in t10)
print(60 not in t10)















