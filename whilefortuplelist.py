# i = 0
# # while and for close by else
# while i < 5:
#     if i == 2:
#         break
#     i += 1
#     print(i)
# else:
#     print("execute else")
#
# for i in range(2, 10):
#     for j in range(2, i):
#         if i % j == 0:
#             print(str(i) + "is not a prime")
#             break
#     else:
#         print(str(i) + "is a prime")
#
# # list
# a = [1, 2, 3]
# # list slice
# # if step is a negative number, the default is form -1 to 0. if you start is lower than end, then return []
# print(a[1:3:-1])
# print(a)

# list func
# heroes = ["hawk", "iron man"]
# heroes.append("spider man")
# chinese_hero = ["sun wu kong", "nv wa"]
# heroes.extend(chinese_hero)
# print(heroes)
#
# a = [1, 2, 3, 4, 5]
# a[len(a):] = [6, 7, 8]
# print(a)
# # use this one
# a[-1:] = [9, 10]
# print(a)
#
# a.insert(0, 0)
#
# # remove 2(item) from a
# a.remove(2)
# # delete the element by index
# a.pop(2)
#
# # a.clear()
# heroes[3:] = ["wu song"]
# print(heroes)
#
# heroes.sort()
# heroes.reverse()
# print(heroes)
#
# print(a.count(3))
# # heroes.index("sun wu kong")
#
# # surface copy
# a1 = a.copy()
# a2 = a[:]
# a[0] = 999
# print(a1, a2)

# note that when you use * to create sub list, the sub list share the same memory
# b = [0] * 6
# b[1] = 2
# print(b)
#
# c = [[0] * 3] * 3
# c[1][1] = 2
# print(c)

# notice that = is quote, not copy
# x = [1, 2, 3]
# y = x
# x[1] = 5
# print(y)
#
# # 浅拷贝只会对最外层进行拷贝，内部元素仍然是引用
# x = [[1, 2, 3], [4, 5, 6]]
# y = x.copy()  # y = x[:] 同理
# x[1][1] = 9
# print(y)
#
# import copy
#
# y = copy.copy(x)  # 浅拷贝
# y = copy.deepcopy(x)  # 深拷贝

# 列表推导式
# [expression for target in iterable]
# [expression for target in iterable if condition]  order: if -> for -> expression
# [expression for target1 in iterable1 for target2 in iterable2]
# order: except expression form left to right(expression the last)
# KISS 原则
# 列表推导式在python脚本中以c语言进行，比正常写法快很多！！！

# x = [1, 2, 3]
# y = [2 * item for item in x]
# print(y)
# # 解决上面浅拷贝问题
# S = [[0] * 3 for i in range(3) if i != 1]
# print(S)
#
# words = ["fantastic", "amazing", "frank", "amen"]
# # 筛选f开头单词
# select = [word for word in words if word[0] == 'f']
# print(select)
#
# flattenS = [col for raw in S for col in raw]
# print(flattenS)

# tuple  () unchangeable
# 没有元组推导式
tup = 1, 2, 3, 4, "lisa"
print(tup[4])
tup[:3]  # support the slice
tup2 = 4, 5
t = tup + tup2  # the concat in tuple
tt = tup, tup2  # the nested in tuple
print(t, tt)

# generate single tuple
single = (222,)
x = (1, "nihao")
age, name = x

ss = "lisa"
a, *b = ss
print(a, b)


