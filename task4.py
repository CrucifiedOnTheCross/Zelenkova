lst = list(map(int, input().split()))
lst.sort(key=lambda x: x % 10)
print(lst)
