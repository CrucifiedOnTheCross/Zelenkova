def f(n):
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


n = int(input())
if f(n) == True:
    print('Prime')
else:
    print('Composite')

M = [[1, 2, 3],
     [5, 6, 7],
     [8, 9, 0]]

# l - строка матрицы M
for l in M:
    # e - элемент строки l
    for e in l:
        # вывыоди элемент матрицы, так, чтобы каждый элемент отделялся пробелом друг от друга
        print(e, end=' ')
    # переходим на новую строку
    print()
