def fun(n):
    temp = 0
    while n:
        print(n)
        print(temp)
        temp= (temp * 10) + (n % 10)
        n = n // 10
        # temp = 
        # print(n)
    print(temp)
    return temp

fun(20)

