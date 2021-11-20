s = int(input())
z = ''
while s != 0:
    z = str(s % 2) + z
    s = s // 2
print(z)
# # for
# print(int(19 / 2))
# print(int(1 / 2))
# print(4 % 2)


# s = input()
# cg = 0
# cc = 0
# for i in range(len(s)):
#     if s[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
#         cg += 1
#     if s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНОПРСТФХЦЧШЩ':
#         cc += 1
# print('Количество гласных букв равно', cg)
# print('Количество согласных букв равно', cc)




# s = input()
# sum1 = 'Цифр нет'
# for i in range(len(s)):
#     if s[i] in '0123456789':
#         sum1 = 'Цифра'
# print(sum1)

# s1 = input()
# s2 = input()
# s3 = input()
# print(s2[0], s1[0], s3[0], sep='')

# s = input()
# for i in range(len(s) - 1, -1, -1):
#     print(s[i])


# s = input()
# for i in range(0, len(s), 2):
#     print(s[i])


# s = 'Python'
# for i in range(len(s) - 1):
#     print(i, s[i])