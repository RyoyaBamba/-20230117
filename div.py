x  = int(input("x = ")) # 入力データ (user input)
y  = int(input("y = ")) # 入力データ (user input)
quotient  = 0  # quotient  = 商
remainder = x  # remainder = 余
while x>=y:
	x-=y
	remainder-=y
	quotient+=1
print("x div y =", quotient)
print("x mod y =", remainder)
