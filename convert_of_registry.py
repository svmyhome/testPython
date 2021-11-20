# s = 'foO BaR BAZ quX.'
# print(s)
# print(s.capitalize()) #первый символ имеет верхний регистр, а все остальные символы имеют нижний регистр.
# print(s.swapcase()) # все символы, имеющие верхний регистр, преобразуются в символы нижнего регистра и наоборот
# print(s.title()) # первый символ каждого слова переводится в верхний регистр.
# print(s.upper()) # все символы имеют нижний регистр.
# print(s.lower()) # все символы имеют верхний регистр.

s = input()
coun = 0
for i in s:
    if i == i.lower() and i not in '01234567890':
        coun += 1
print(coun)


# s = input().lower()
# if "хороший" in s:
#     print("YES")
# else:
#     print("NO")

    # s = input()
# print(s.swapcase())


# s = input()
# if s.title() == s:
#     print("YES")
# else:
#     print("NO")

