def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


a, b = map(int, input().split())
print(nod(a, b))
