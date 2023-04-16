a = ord("A")
print("A translate to unicode code", a)
a = ord("中")
print("中 translate to unicode code", a)


a = chr(65)
print("65 translate to one character", a)
a = chr(25991)
print("255991 translate to one character", a)


a = "ABC".encode("ascii")
print("ABC encode ascii:", a)
a = "ABC".encode("utf-8")
print("ABC encode utf-8:", a)


a = "中文".encode("utf-8")
print("中文 encode utf-8", a) # 可以看到每个中文占了三个字节


# decode 是将字节流(bytes)转换为 str
a = b'ABC'.decode('utf-8')
print("bABC decode utf-8", a)

a = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print("\\xe4\\xb8\\xad\\xe6\\x96\\x87 decode utf-8", a)


# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len("中文"))
print(len("中文".encode("utf-8")))
