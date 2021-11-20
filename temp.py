n = int(input())
x = 'YES'
while len(str(n)) > 1:
    # if n % 10 == (n // 10) % 10 and n > 1:
    #     n = n // 10
    if n % 10 > (n // 10) % 10:
        x = 'NO'
        n = n // 10
    n = n // 10
print(x)


# t = int(input())
# sum2 = 0
# while t != 0:
#     if int(len(str(t))) - 1 == 1:
#         sum2 = t % 10
#     t = t // 10
# print(sum2)

# n = int(input())
# x = 'YES'
# while len(str(n)) > 1:
#     # if n % 10 == (n // 10) % 10 and n > 1:
#     #     n = n // 10
#     if n % 10 != (n // 10) % 10:
#         x = 'NO'
#         n = n // 10
#     n = n // 10
# print(x)


# n = int(input())
# while n > 9:
#     x = n % 10
#     n = n // 10
# print(x)


# t = int(input())
# sum1 = 0
# counter = 0
# mult1 = 1
# l1 = int(str(t)[0])
# last = t % 10
# while t != 0:
#     counter += 1
#     sum1 += t % 10
#     mult1 *= t % 10
#     t = t // 10
# print(sum1)
# print(counter)
# print(mult1)
# print(sum1 / counter)
# print(l1)
# print(l1 + last)



# t = int(input())
# i = 0
# j = t
# while t != 0:
#     x = t % 10
#     if i < x:
#         i = x
#     if j > x:
#         j = x
#     t = t // 10
# print(f'Максимальная цифра равна {i}')
# print(f'Минимальная цифра равна {j}')

# x = input()
# print(f'Максимальная цифра равна {max(x)}')
# print(f'Минимальная цифра равна {min(x)}')



# t = int(input())
# while t != 0:
#     print(t % 10, end="")
#     t = t // 10

# t = int(input())
# while t != 0:
#     print(t % 10)
#     t = t // 10


# t = int(input())
# i = 0
# while 0 != t:
#     if 25 <= t:
#         t -= 25
#         i += 1
#     elif 10 <= t:
#             t -= 10
#             i += 1
#     elif 5 <= t:
#             t -= 5
#             i += 1
#     elif 1 <= t:
#         t -= 1
#         i += 1
# print(i)


# t = int(input())
# while 0 == t % 7:
#     print(t)
#     t = int(input())

# t = int(input())
# i = 0
# while 0 <= t:
#     i += t
#     t = int(input())
# print(i)

# t = int(input())
# i = 0
# while 5 >= t >= 0:
#     if t == 5:
#         i += 1
#     t = int(input())
# print(i)
