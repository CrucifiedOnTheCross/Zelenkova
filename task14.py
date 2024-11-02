file = input().split()
lst_search = ['a', 'an', 'the', '']
c = 0
for el in file:
    if el.lower() in lst_search:
        c += 1
print('Общее количество артиклей:', c)
