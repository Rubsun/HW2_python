n = int(input())
s = 0
for i in range(n):
    number = int(input())
    if number == 0:
        s += 1
if s > 0:
    print("YES")
else:
    print("NO")