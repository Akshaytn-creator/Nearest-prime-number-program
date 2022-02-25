def prime(n):
    prime = True
    if n < 2:
        prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
    return prime
n = int(input("ENTER A USER NUMBER:"))
flag, i = True, 1
if prime(n):
    print("CLOSEST PRIME NUMBER IS :", n)
else:
    while flag:
        if prime(n + i) and prime(n - i):
            print(n - i, 'and', n + i, 'are closest prime numbers')
            flag = False
        elif prime(n - i):
            print('CLOSEST PRIME NUMER =', n - i)
            flag = False
        elif prime(n + i):
            print('CLOSEST PRIME NUMBER =', n + i)
            flag = False
        i += 1