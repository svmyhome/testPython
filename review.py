count = 0
p = 1
for i in range(1, 4):
    x = int(input())
    if x > 0:
        p = p * x
        count += 1
if count < 10:
    print('NO')
    print(p)
else:
    print(count)
    print(p)