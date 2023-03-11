n = int(input())
count = 0

for i in range(1, n + 1):
    if n % i == 0: #Если число делится нацело
        count += 1 #Кол-вл +один

print(count)
