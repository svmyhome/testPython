mx = 0
s = 0
for _ in range(10):
    x = int(input())
    if x < 0:
        s += x
        if x > mx:
            mx = x
if s == 0:
    print('NO')
else:
    print(s)
    print(mx)