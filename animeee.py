import time
img0 = 10000000000011

t = 0

print(img0)

i = 0
img0 += 10 ** (12 - i)
i += 1

time.sleep(0.1)
t += 1

while i < 11:
    print(img0)
    img0 = img0 + 10**(12 - i) - 10**(13 - i)
    i += 1
    time.sleep(0.1)
    t += 1

print(img0)

img0 = img0 - 111
time.sleep(0.1)
t += 1

while t < 29:
    print(img0)
    img0 = img0 + 11
    time.sleep(0.1)
    t += 1
    print(img0)
    img0 = img0 - 11
    time.sleep(0.1)
    t += 1
