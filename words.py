'''
Напишите программу, которая считывает строку с числом nn, которое задаёт количество чисел, которые нужно считать.
Далее считывает nn строк с числами x_ix i ​
 , по одному числу в каждой строке. Итого будет n+1n+1 строк. При считывании числа x_ix i ​
  программа должна на отдельной строке вывести значение f(x_i)f(x i ​  ). Функция f(x) уже реализована и доступна для вызова.
Функция вычисляется достаточно долго и зависит только от переданного аргумента xx.
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.
'''

n = int(input())
l = []
for i in range(n):
    l += int(input())
print(l)



'''
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова,
разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального
слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.
'''

# n = input().lower().split()
# d = {}
# for key in n:
#     if key not in d:
#         d[key] = 1
#     elif key in d:
#         d[key] += 1
# for key, value in d.items():
#     print(key, value)

'''
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и valuevalue.

Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. Если и ключа 2 * key2∗key
 нет, то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].

Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.
'''
# d = {}
# # print(d[1])
# # print(d.keys())
#
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     else:
#         if 2 * key in d:
#             d[2 * key] += [value]
#         elif 2 * key not in d:
#             d[2 * key] = [value]
#
#
# update_dictionary(d, 1, -1)
# print(d)
# update_dictionary(d, 2, -2)
# print(d)
# update_dictionary(d, 1, -3)
# print(d)

# Словари
# l = ['hold', 'held', 'held']
# d = {'держать': l, 'знать': 'know, knew, known'}
# print(d)
# print('держать' in d)
# print('держать1' not in d)
# d['вести'] = 'lead, led, led'
# print(d)
# print(d['вести'])
# print(d.get('вести1'))
#
# for x in d:
#     print(x, end=" ")
# print()
#
# for x in d.keys():
#     print(x,  end=" ")
# print()
# for x in d.values():
#     print(x, end=" | ")
# print()
#
# for x,y in d.items():
#     print(x, y, end=" | ")
# print()

#  Списки
# c = set()
# # c  {'1','6', '2'}
# c.add('4')
# c.add('5')
# c.add('7')
# c.add('1')
# basket = {'apple', 'orange', 'pinats', 'orange', 'donuts'}
# print(basket)
# print(c)
# print(len(c))
# c.remove('7')
# print(c)
# c.discard('1')
# print(c)
# c.clear()
# print(c)
# print('orange' in basket)
# print('pie' in basket)
#
# for x in basket:
#     print(x)
