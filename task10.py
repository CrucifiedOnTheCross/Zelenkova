M = []
n = int(input())
for i in range(n):
    M.append(list(map(int, input().split())))

for l in M:
    avg = sum(l) / len(l)
    c = 0
    for el in l:
        if el > avg:
            c += 1
    print(c)
