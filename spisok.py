'''
Напишите программу, которая принимает на вход список чисел в одной строке
и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''

s = [int(i) for i in input().split()]
m = 0
j = 1
str1 = ''
s.sort()
if len(s) == 2:
    if s[m] == s[j]:
        str1 += str(s[m])
elif len(s) > 2:
    while len(s) > j:
        if s[m] != s[j]:
            m += 1
            j += 1
        elif s[m] == s[j]:
            while s[m] == s[j] and s[j] != len(s) - 1:
                if j >= len(s) - 1:
                    break
                j += 1
                if j >= len(s) - 1:
                    break
            str1 += str(s[m])
            m = j
            j += 1
            if j < len(s):
                str1 += " "
            if j > len(s) - 1:
                break
print(str1)
'''
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''
# n = [int(i) for i in input().split()]
# m = 0
# sum = 0
# str1 = ''
# while len(n) > m:
#     if len(n) == 1:
#         str1 = n[m]
#         break
#     if len(n) == 2:
#         str1 = str(n[m + 1] *2)  + " " +  str(n[m] * 2)
#         break
#     if len(n) > 2:
#         if m == 0:
#             sum = n[1] + n[len(n) - 1]
#             str1 += str(sum) + " "
#         if 0 < m < len(n) - 1:
#             sum = n[m - 1] + n[m + 1]
#             str1 += str(sum) + " "
#         if m == len(n) - 1:
#             sum = n[0] + n[len(n) - 2]
#             str1 += str(sum)
#     m += 1
# print(str1)

# a = [int(i) for i in input().split()]
# b = 0
# for i in a:
#     b += i
# print(b)


# students = ['Masha','Saha', 'Petya']
# prepods = ['Sidor', 'Nikolaq']
#
#
# print(students[1])
# print(students[-1])
# print(students[:2])
# print(students[::-1])
#
# print(students + prepods)
# print(prepods * 2)
#
# students.append('PIOTR')
# students += ['Evgen', 'Zamud']
# students.insert(1,'98324h23hb42jh')
# students += 'Olga'
# students.remove('O')
# del students[8]
# print(students)
# for i in students:
#     print('Hello', i)
#
# if 'Saha' in students:
#     print('Yes')
# if 'Olga' not in students:
#     print('NO')
#
# print(students.index('Petya'))
# st2 = ['Sidor', 'Nikolaq', 'Evgen', 'Zamud']
# print(sorted(students))
# st2.sort()
# print(st2)
# print(min(students))
# print(min(st2))
# print(max(st2))
# print(st2.reverse())
# print(reversed(students))
#
# a = [i*i for i in range(5)]
# print(a)
# b = [str(i) for i in input().split()]
# print(b)
