from random import randint
#import time

#start_time = time.time()


def search(x, y): # функция бинарного поиска
#    start_time = time.time()
    low = 0
    high = len(x) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = x[mid]
        if guess == y:
            return mid + 1
        elif guess > y:
            high = mid - 1
        else:
            low = mid + 1

x = []
for i in range(10):#рандомим числа в массиве
    x.append(randint(1,1000))
x.sort()
print(x)
value = int(input("введите значение которое нужно найти= "))
print("result = ", search(x, value))
#print("--- % s seconds ---" % (time.time() - start_time))        
