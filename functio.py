lst = [int(i) for i in input().split()]
def modify_list(l):
    l[:] = [x // 2 for x in l if x % 2 == 0]
    # n = []
    # for i in range(len(l)):
    #     if l[i] % 2 == 0:
    #         n.append(l[i])
    # l.clear()
    # for i in range(len(n)):
    #     l.append(n[i] // 2)
    print(l)
    print(len(l))
modify_list(lst)




# def min2(a,b):
#     if a <= b:
#         return  a
#     else:
#         return b
#
# print(min2(2,3))
#
# def f(n):
#     return n * 10 + 5
#
# print(f(f(f(10))))