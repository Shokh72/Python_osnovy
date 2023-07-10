def power(a, n):
    if n==0:
        return 1
    elif n<0:
        q = abs(n)
        return 1/(a*power(a,q-1))
    else:
        return a*power(a, n-1)

a = float(input("a = "))
n = float(input("n = "))
print(power(a, n))