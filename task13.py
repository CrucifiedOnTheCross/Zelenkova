n = int(input())
m = int(input())

Mat = []
for i in range(n):
    line = []
    for j in range(m):
        line.append(input())
    Mat.append(line)

for line in Mat:
    print(' '.join(line))

print()

for j in range(m):
    for i in range(n):
        print(Mat[i][j], end=' ')
    print()