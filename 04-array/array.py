a = [1, 2, 3]
print("a = ", a)
print("length of a = %d" % len(a))

print("a[0] = %d" % a[0])

a.append(4)
print("append element 4 to a: ",a)

a.insert(0, 0)
print("insert element 0 to a: ", a)

a.pop(0);
print("pop the first element to a: ", a)


a[0] = "has change"
print("update element: ", a)

b = [1, 2, 3, [1, 2]]
print("b =", b)
print("b[3][0] = ", b[3][0])