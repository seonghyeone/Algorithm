a = input()
num = [2, 3, 4, 5, 6, 7, 8, 9]
Long_eng = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
made_list = []

for b in a:
    for index, eng in enumerate(Long_eng):
        for p in eng:
            if b in p:
                made_list.append(num[index])

print(sum(made_list) + len(made_list))