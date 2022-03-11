a, b = map(int, input().split())
c = int(input())


h, m = divmod(b + c, 60)
#h에 몫이 m에 나머지가 들어감 b + c를 안더하면 자릿수 넘어가는걸 고려해줘야됨
if a + h == 24:
    print(0, m)

else:
    print(a + h, m)