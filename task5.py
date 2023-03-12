max = 0
count = 1
number = int(input())
while number != 0:
    if number > max:  #Замена числа на максимальное и обнуление счетчика
        max = number
        count = 1
    elif number == max:
        count += 1

    number = int(input())
print(count)