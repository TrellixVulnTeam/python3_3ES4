def power(n=2, x):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))