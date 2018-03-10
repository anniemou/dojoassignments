#1

for i in range(1,1000, 2): 
    print i
#Multiple of 5
for i in range(5,1000000):
    if (i % 5 == 0):
        print i

#2.
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum

#3.
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum/len(a)
