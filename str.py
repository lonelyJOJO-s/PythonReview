# func
# x = "i love you, baby"
# x = x.capitalize()  # 第一个单词首字母大写
# print(x)
# x = x.casefold()  # all to lower
# print(x)
# x.title()  # all first to upper, else to lower
# x.swapcase()
# x.upper()
# x.lower()
# x.center(15)
# x.ljust(15)
# x.rjust(15)
# x.zfill(15)  # fill zero in the beginning
#
# print(x.count('o'))
# print(x)
# x.replace("love", "hate", -1)
#
# print(x)
#
# #  判断回文
# sentence = "上海自来水来自海上"
# if sentence[::-1] == sentence:
#     print(sentence + "is a echo sentence")
# print(sentence.startswith("上海"))
# sentence.endswith("海上")
# # any one
# sentence.startswith(("上海", "广东"))

x = "2²"
x = "Ⅰ Ⅱ"
x = "一二三四"
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())
x.isalnum()  # 上面三个的中核

''' str 的截取  '''
x = "  ".lstrip("你要去除的字符集合，默认为空格")
x = "asdeoawkd".rstrip("kdw")
print(x)
print("ssad.com".removesuffix(".com"))

# return a three tuple,
"www.xxx.com".partition(".")

"hello nihao".split("指定分割符")

# divide by line
"  ".splitlines()

# join is much quicker than +
'.'.join(["www", "whut", "edu"])

# 格式化字符串

lover = "you"
who = "i"
print("{0} love {1}".format(lover, who))

# align
# '<' 默认左对齐
# '>' 默认右对齐
# '^' 居中对齐

print("{:^10}".format(520))

print("{1:>10} {0:<10}".format(520, 250))
# % 为填充字符
print("{1:%>10} {0:%<10}".format(520, 250))

# 小数点后显示几位
"{:.2f}".format(3.1415)
# 总计显示几位
"{:.2g}".format(3.1415)
# 只能用于字符串
"{:.6}".format("select")
"{:2%}".format(0.9888)

# f-string
# 对format的简化
print(f"1+1={1+1}")
print(f"{520:010}")

