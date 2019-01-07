def factorial(k):
    if k == 0:
        return 1
    else:
        return k * factorial(k-1)


sum = 0
for k in range(1, 800):
    a = 0
    for l in range(0, k):
        a += (-1)**(k-l)*2**l
    sum += (2**k+a)/factorial(k)
print(sum)