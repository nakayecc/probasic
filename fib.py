
i = 0
j = 1
k = 0
fib = 0


tmp = int(input("How many numbers ?: "))

while (i < tmp):
    
    if (tmp <50 ):
        print( '{0:2d}:{1:15d}'.format(i+1,fib))
    elif (tmp > 50):
        print( '{0:2d}:{1:30d}'.format(i+1,fib))
    fib = j+k
    j = k
    k = fib
    i = i + 1