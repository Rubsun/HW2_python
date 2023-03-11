n = int(input())
summ = 1
factorial = 1


for i in range(1, n + 1):
    factorial *= i #Находим Факториал
    numb = 1/factorial
    summ += factorial
print(summ)