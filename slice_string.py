# s = 'abcdefghij'
# print("-" * 10, "Положительные", "-" * 10)
# print(s[:]) # выводит всю строку
# print(s[0:6]) # выводит значения от 0 до 6
# print(s[3:10]) # выводит значения от 3 до 9
# print(s[:6]) # выводит значения от начала и до 6
# print(s[3:]) # выводит значения от 3 до конца
# print("-" * 10, "Отрицательные", "-" * 10)
# print(s[-8:-1]) # выводит значения от 3 до предпоследнего
# print(s[-5:]) # выводит значения от -5 до конца
# print(s[:-5]) # выводит значения от 1 до  -5
# print("-" * 10, "Шаг", "-" * 10)
# print(s[0:7:2]) # выводит значения от 0 до 7 c шагом 2
# print(s[0::2]) # выводит значения от 0 до конца c шагом 2
# print(s[-9:-1:2]) # выводит значения от -9 до -1 c шагом 2
# print(s[-9::2]) # выводит значения от -9 до конца c шагом 2
# print(s[::-1]) # выводит значения в обратнм порядке
# print(s[::-2]) # выводит значения в обратном порядке с шагом 2
# print(s[:4] + '4' + s[5:]) # выводит значения с изененным значением

s = input()
print(s[len(s) - (len(s) // 2):]+s[:len(s) - (len(s) // 2)])
# print(s[2])  # третий символ этой строки;
# print(s[-2])  # предпоследний символ этой строки;
# print(s[:5])  # первые пять символов этой строкиё;
# print(s[:-2])  # всю строку, кроме последних двух символов;
# print(s[::2])  # все символы с четными индексами.
# print(s[1::2])  # все символы с нечетными индексами;
# print(s[::-1])  # все символы в обратном порядке;
# print(s[::-2])  # все символы строки через один в обратном порядке, начиная с последнего.


# s = input()
# print(s[2])  # третий символ этой строки;
# print(s[-2])  # предпоследний символ этой строки;
# print(s[:5])  # первые пять символов этой строкиё;
# print(s[:-2])  # всю строку, кроме последних двух символов;
# print(s[::2])  # все символы с четными индексами.
# print(s[1::2])  # все символы с нечетными индексами;
# print(s[::-1])  # все символы в обратном порядке;
# print(s[::-2])  # все символы строки через один в обратном порядке, начиная с последнего.

# s = input()
# print(len(s))  # общее количество символов в строке;
# print(s * 3)  # исходную строку повторенную 3 раза;
# print(s[0])  # первый символ строки;
# print(s[:3])  # первые три символа строки;
# print(s[-3:])  # последние три символа строки;
# print(s[::-1])  # строку в обратном порядке;
# print(s[1:-1])  # строку с удаленным первым и последний символом.

# s = input()
# s1 = "YES"
# if s != s[::-1]:
#     s1 = "NO"
# print(s1)



# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::7])
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[:12])





