#example
s={1,2,'a','codegnan'}
print(s)

#empty set
s1={}
s2=set()
print(type(s1),type(s2))

#set methods
s={1,2,3,4}
s.add(100)
print(s)
s.update([10,20])
print(s)
s.remove(2)
print(s)
s.discard(100)
print(s)
val=s.pop()
print(val,s)
s.clear()
print(s)

#union ,interssecton,difference,symmetric diffrence
s1={1,2,3,4}
s2={3,4,5,6}
union=s1.union(s2)
print(s1.union(s2))
intersection=s1.intersection(s2)
difference=s1.difference(s2)
symmetric_difference=s1.symmetric_difference(s2)
print(union,intersection,difference,symmetric_difference)

#issubset(),issuperset(),isdisjoint()
s1={1,2,3,4,5,6}
s2={3,4,5,6}
print(s1.issubset(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))
