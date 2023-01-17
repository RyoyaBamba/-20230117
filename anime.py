import time

img0 = 100000000000000000000000000000000000000
img1 = 100000000000000000000000000000000000011
img2 = 100000000000000000000000000000000000011
img3 = 111000000000000000000000000000000000111
img4 = 111000000000000000000000000000000011111
img5 = 111110000000000000000000000000000011111
img6 = 111000000000000000000000000000000000111
img7 = 111000000000000000000000000000000000011
img8 = 100000000000000000000000000000000000011
img9 = 100000000000000000000000000000000000000

print(img0)
print(img1)
print(img2)
print(img3)
print(img4)
print(img5)
print(img6)
print(img7)
print(img8)
print(img9)

t = 0
i = 0
img5 += 10 ** (33 - i)
i += 1
time.sleep(0.01)
t += 1

while i < 29:
    print(img0)
    print(img1)
    print(img2)
    print(img3)
    print(img4)
    print(img5)
    print(img6)
    print(img7)
    print(img8)
    print(img9)
    img5 = img5 + 10**(33 - i) - 10**(34 - i)
    i += 1
    time.sleep(0.01)
    t += 1

print(img0)
print(img1)
print(img2)
print(img3)
print(img4)
print(img5)
print(img6)
print(img7)
print(img8)
print(img9)

img1 = img1 - 11
img2 = img2 - 11
img3 = img3 - 111
img4 = img4 - 11111
img5 = img5 - 111111
img6 = img6 - 111
img7 = img7 - 11
img8 = img8 - 11

time.sleep(0.1)
t += 1

while t < 43:
    print(img0)
    print(img1)
    print(img2)
    print(img3)
    print(img4)
    print(img5)
    print(img6)
    print(img7)
    print(img8)
    print(img9)
    img1 = img1 + 11
    img2 = img2 + 11
    img3 = img3 + 111
    img4 = img4 + 11111
    img5 = img5 + 11111
    img6 = img6 + 111
    img7 = img7 + 11
    img8 = img8 + 11
    time.sleep(0.1)
    t += 1
    print(img0)
    print(img1)
    print(img2)
    print(img3)
    print(img4)
    print(img5)
    print(img6)
    print(img7)
    print(img8)
    print(img9)
    img1 = img1 - 11
    img2 = img2 - 11
    img3 = img3 - 111
    img4 = img4 - 11111
    img5 = img5 - 11111
    img6 = img6 - 111
    img7 = img7 - 11
    img8 = img8 - 11
    time.sleep(0.1)
    t += 1
   
