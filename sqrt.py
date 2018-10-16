def sqrt(a):
    x0 = 0
    while x0**2 < a:
        x0 += 1
        print(x0)
    if x0**2 == a:
        return x0
    else:
        root = x0
        for i in range(0, 20):
            root = (a - root**2 + 2 * root**2) / (2 * root)
        return root


print(sqrt(2))