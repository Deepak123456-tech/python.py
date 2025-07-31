n = 4
for i in range(0, n):
    print(i)


li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])
else:
    print("Inside Else Block")

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")


cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello ")
else:
    print("In Else Block")


while (True):
    print("Hello ")

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


for letter in 'gets':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)



for letter in 'gets':
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)


for letter in 'gets':
    pass
print('Last Letter :', letter)











    
