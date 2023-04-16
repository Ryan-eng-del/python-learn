print('''line1
line2
line3''')

# python 动态类型语言，编译时不会检查类型，解释执行时才会报错

a = 1
a = True
a = "str"
a = None
a = 1.2

print(True and True)
print(True or False)


a = 'ABC'
b = a
a = 'XYZ'
print(b)
print("Hello %s" % "world")