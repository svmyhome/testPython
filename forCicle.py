'''
Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и выводит
на консоль среднее арифметическое всех чисел из отрезка [a; b][a;b], которые кратны числу 33.
В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [-5; 12][−5;12].
Всего чисел, делящихся на 33, на этом отрезке 66: -3, 0, 3, 6, 9, 12−3,0,3,6,9,12. Их среднее арифметическое равно 4.54.5
На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 33.﻿
'''

a = int(input())
b = int(input())
j = 0
s = 0
for i in range(a, b+1):
    if (i % 3 == 0):
        s += i
        j += 1
print(s/j)





'''
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками.
Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке.
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].
Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a \le ba≤b, c \le dc≤d.
Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
Заметьте, что левым столбцом и верхней строкой выводятся сами числа
из заданных отрезков — заголовочные столбец и строка таблицы.
'''

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for j in range(c, d + 1):
#     print(' ', j, end='')
# for i in range(a,b+1):
#     print()
#     print(i, end='')
#     for j in range(c,d+1):
#         print('', i * j, end='')
#
# a, b = (int(i) for i in input().split())
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b+1, 2):
#     s += i
# print(s)



# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a,b+1,2):
#     s += i
# print(s)


# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# for i in range(a, b+1):
#     if (i % 2 == 1):
#         s += i
# print(s)



# for i in 2,3,4:
#     print(i*i)

# for i in range(10):
#     print(i * i)

# for i in range(2,5):
#     print(i * i)

# for i in range(2,15,4):
#     print(i)

# n = int(input())
# for i in range( n ):
#     print('*' * n)

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print('*',end='')
#     print()
