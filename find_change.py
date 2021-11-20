# s = '     foo goo moo    '
# print(s)
# print("-" * 10, "COUNT", "-" * 10)
# print(s.count("oo")) # показывает количество вхождений
# print(s.count("oo", 2)) # показывает количество вхождений со 2 позиции
# print(s.count("oo", 2, 7)) # показывает количество вхождений со 2 по 7 позиции
# print("-" * 10, "STARTWITH", "-" * 10)
# print(s.startswith("oo")) # определяет начинается ли исходная строка c с подстроки False или True
# print(s.startswith("fo")) # определяет начинается ли исходная строка c с подстроки False или True
# print("-" * 10, "ENDSWITH", "-" * 10)
# print(s.endswith("oo")) # определяет заканчивается ли исходная строка c с подстроки False или True
# print(s.endswith("fo")) # определяет заканчивается ли исходная строка c с подстроки False или True
# print("-" * 10, "FIND RFIND", "-" * 10)
# print(s.find("go")) # находит индекс первого вхождения подстроки
# print(s.rfind("fo")) # находит индекс первого вхождения подстроки
# print(s.rfind("yo")) # находит индекс первого вхождения подстроки в случае ошибки выдает -1
# print("-" * 10, "index Rindex", "-" * 10)
# print(s.index("go")) # находит индекс первого вхождения подстроки
# print(s.rindex("fo")) # находит индекс первого вхождения подстроки
# #print(s.index("yo")) # находит индекс первого вхождения подстроки в случае ошибки валится в ошибку лучше использовать find rfind
# print("-" * 10, "STRIP, LSTRIP, RSTRPI", "-" * 10)
# print(s.strip()) # удалены все пробелы стоящие в начале и конце строки.
# print(s.rstrip()) # все пробелы стоящие в конце строки.
# print(s.lstrip()) # все пробелы стоящие в начале строки.
# print("-" * 10, "REPLACE", "-" * 10)
# print(s.replace("oo", "II")) # возвращает копию s со всеми вхождениями подстроки <old>, замененными на <new>
# print(s.replace("oo", "II", 2)) #может принимать опциональный третий аргумент <count>,  который определяет количество замен.

s = input()
x1 = s.find("h")
x2 = s.rfind("h")
print(s[:x1] + s[x2 + 1:])


# s = input()
#
# if s.count("f") == 1:
#     print(s.find("f"))
# elif s.count("f") >= 2:
#     print(s.find("f"), s.rfind("f"))
# else:
#     print("NO")



# s = input()
# n = 0
# c = ""
# for i in s:
#     if n <= s.count(i):
#         n = s.count(i)
#         c = i
# print(c)

# s = int(input())
# n1 = 0
# for _ in range(s):
#     s1 = input()
#     if s1.count('11', 0, len(s1)) >= 3:
#         n1 += 1
# print(n1)

# s = int(input())
# n1 = 0
# s2 = ""
# ns = ""
# for _ in range(s):
#     s1 = input()
#     # print(s1.count('11', 0, len(s1)))
#     for i in s1:
#         if "1" == i:
#             ns = ns + i
#     # print(ns)
#     if ns.count('11', 0, len(ns)) >= 3:
#         n1 += 1
# print(n1)

# s = input()
# n = 0
# for i in "0123456789":
#     n += s.count(i)
# print(n)


# s = input()
# if s.endswith(('.com', '.ru')):
#     print("YES")
# else:
#     print("NO")




# s = input().lower()
# print("Аденин:", s.count("а"))
# print("Гуанин:", s.count("г"))
# print("Цитозин:", s.count("ц"))
# print("Тимин:", s.count("т"))

# s = input().lower()
# print("Аденин:", s.count("а"))
# print("Гуанин:", s.count("г"))
# print("Цитозин:", s.count("ц"))
# print("Тимин:", s.count("т"))


# s = input()
# print(s.count(" ") + 1)


