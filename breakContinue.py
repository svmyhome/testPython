'''
Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.
'''

i = 0
while True:
    i = int(input())
    if i < 10:
        continue
    elif i > 100:
        break
    print(i)



# i = 0
# while i < 5:
#     a, b = input().split()
#     a = int(a)
#     b = int(b)
#     if (a == 0 and b == 0):
#         break
#     if (a == 0 or b == 0):
#         print('print 1')
#         continue
#     print(a * b)
#     i += 1