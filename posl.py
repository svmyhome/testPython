s = 0 #
for _ in range(1, 8): #
    n = int(input())
    if n % 2 == 0: #
        s += n #
if s == 0:
    print(0)
else:
    print(s)