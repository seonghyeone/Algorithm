a, b, c = map(int, input().split())

if c - b > 0:
    y = int(a / (c - b)) + 1
    print(y)
else:
    print(-1)

