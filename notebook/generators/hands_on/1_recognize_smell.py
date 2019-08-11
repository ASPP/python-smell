for i in range(9):
    if i % 3 == 0:
        continue
    print('Square is', i ** 2)

for j in range(5):
    if j % 2 == 0:
        continue
    print('Cube is', j ** 3)

for k in range(13):
    if k % 5 == 0:
        continue
    print('A' * k)
