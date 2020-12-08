# # a3b4c2e10b1
# with open('words.txt', 'r') as inf:
#     str1 = inf.readline().strip()
# print(str1)
# # y = 0
# i = 0
# j = 1
# n = 0
# str_all=''
# while len(str1) > n:
#     str_all += (str1[y:i] * int(str1[i:j]))
#     print(str_all)
#     y += 2
#     i += 2
#     j += 2
#     n += 1
# print(str1[y:i] * int(str1[i:j]))


with open('1.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
        print(line)




# with open('1.txt', 'w') as out:
#     out.write('ldcsdlkmcvkldsma;lcx,as;,cvasmvs alkvmnkjv  vndanvjksnvjk edrjknvjnvjknvnmmdjnvjk\n')
#     out.write(str(92384892348237423897)+'\n')
#     out.write(str(10323423423454463546))
# with open('1.txt', 'r') as inf:
#     for line in inf:
#         line = line.strip()
#         print(line)


# import os
# inf = open('1.txt', 'r')
# s1 = inf.readline()
# s2 = inf.readline()
# inf.close()
# print(s1, s2)
# print('-----------------')
# with open('1.txt', 'r') as inf:
#     s1 = inf.readline()
#     s2 = inf.readline()
# print(s1, s2)
# print('-----------------')
# with open('1.txt', 'r') as inf:
#     s1 = inf.readline().strip() # убирает лишние знаки невидимые
#     s2 = inf.readline()
# print(s1, s2)
#
# print(os.path.join('c','dir1','dir2'))