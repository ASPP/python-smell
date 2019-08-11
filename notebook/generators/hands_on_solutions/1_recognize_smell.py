def range_without_multiples(n, base):
    for i in range(n):
        if i % base == 0:
            continue
        else:
            yield i

for i in range_without_multiples(n=9, base=3):
    print('Square is', i ** 2)

for j in range_without_multiples(n=5, base=2):
    print('Cube is', j ** 3)

for k in range_without_multiples(n=13, base=5):
    print('A' * k)

