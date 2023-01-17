n=int(input("n = "))
print("----------")

if n<0 or n>50:
    print(f"bad value of n ({n})")
    exit (1)

total=0
while n>=0:
    print(f"n = {n}")
    n=n-1
    total=total+1

print("done.")
print(f"total = {total} iterations")
