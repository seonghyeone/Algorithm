import math

a, b, c = map(int, input().split())

if c - b > 0:
    y = a // (c - b)
    if int(y) == y:
        print(y + 1)
    else:
        print(math.ceil(y))
else:
    print(-1)

