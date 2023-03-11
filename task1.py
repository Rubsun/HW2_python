n = int(input())
s = 2
while s <= 3000 and s >= 2: #Ограничение
    if n % s == 0:
        print(s)
        break
    else:
        s += 1