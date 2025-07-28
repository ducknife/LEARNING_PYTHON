
str = input()
n_th, n_ha = 0, 0
for i in  str:
    if i.upper() != i:
        n_th += 1
    else:
        n_ha += 1
if n_th >= n_ha:
    print(str.lower())
else:
    print(str.upper())