t = (19, 42, 21)
print(f'The {len(t)} numbers are: ', end='')
for i in t[:-1]:
    print(i, end=', ')
print(f'{t[-1]}')
