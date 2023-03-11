n = int(input())

count = 0
sum = 0

while n > 0:
    count +=1
    sum +=n
    n = int(input())

fin = sum/count
print(fin)