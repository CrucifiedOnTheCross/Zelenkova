lst = list(map(int, input().split()))
lst.sort()

flag = True
for i in range(len(lst) - 1):
    if lst[i] == lst[i + 1]:
        flag = False
        break

if flag == True:
    print("yes")
else:
    print("no")