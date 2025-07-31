#list
#create empty list
#l=[]
#l1=list()
#print(type(1),type(l1))

#l2=[0]
#len(l2)

#read list of element from user
#l3=list(map(int,input().split()))
#print(l3)

#mutable
#l3[0]

#index based and sliceable
l=[1,2,3,'a','b',5.5,6,1,2,3]
print(l[0])
print(l[-1])
print(l[5])

#concasation
l1=[1,2,3]
l2=[4,5]
print(l1+l2)

#list repetition using *
l3=[1,2,3]
print(l3*3)

#list methods
l4=[1,2,3,'3a','b',5.5,6,1,2,3]
#append(),extend(),insert()
print(l4)
l4.append(100)
print(l4)
l4.extend([200,300])
print(l4)
l4.insert(4,'codegnan')
print(l4)

#remove(),pop(),clear(),del()
l4.remove(2)
print(l4)
l4.pop()
print(l4)
l4.pop(3)
print(l4)
del l4[0]
print(l4)
del l4[2:4]
print(l4)
l4.clear
print(l4)

#len(),max(),min(),count(),sum(),sort(),reverse()
l5=[1,2,3,6,1,2,3]
min_value=min(l5)
print(min_value)
max_value=max(l5)
count_2=l5.count(2)
sum_list=sum(l5)
print(max_value)
print(count_2)
print(sum_list)

#sort(),reverse()
l5.sort()
print(l5)
l5.reverse()
print(l5)

#nested list()
l6=[1,2,3,[4,5,6],[7,[8,9],10]]
l6[2]
l6[3][1]
l6[4][1][0]

        






print(l4)



