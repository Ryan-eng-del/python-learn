a = (1, 2, 4)
print("a is tuple", a)
a = (1,)
print("a is tuple which only has one element: ", a)
a = (1, [2, 3])
print("understand tuple is immutable", a)

a[1][0] = "change"
a[1][1] = "change"
print("tuple is change in a certain cases", a)
