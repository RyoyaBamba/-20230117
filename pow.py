a = int(input("a = "))
x = int(input("x = "))
y = a

for i in range(x-1):
    y *= a

print("a**x =", y)
