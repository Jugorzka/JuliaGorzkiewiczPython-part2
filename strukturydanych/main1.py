x = ( 10, -3, 4, 9, 12, -6, 0)
max_licz = x[0]
min_licz = x[0]
for licz in x:
    if licz > max_licz:
        max_licz = licz
    if licz < min_licz:
        min_licz = licz
print(f'Największa liczba to: {max_licz}')
print(f'Najmniejesza liczba to: {min_licz}')


