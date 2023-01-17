def swap(array, i, j):
    if i == j: return
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def sort_inplace(a):
    for i in range(len(a)):
        for j in range(i-1, -1, -1):
            if a[j] > a[j+1]:
                swap(a, j, j+1)
    return a

a = ['a','b','c','d','e','f']
print(f"IN : {a}")
swap(a, 2, 4)
print(f"OUT: {a}")
