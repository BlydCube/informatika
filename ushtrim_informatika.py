# S = 2-4+8-16...
n = int(input('termi i n-te: '))

def fuqi_katres(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 4 != 0):
                return False
            n = n // 4
    return True

def g(n):
    return(2 ** n)

list = [g(i) for i in range (1, n+1, 1)]
list = [-a if fuqi_katres(a) == True  else a for a in list]
sum = 0
for i in list:
    sum += i
    i+= 1
print(list)
print(sum)
