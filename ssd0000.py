def search(data, left, right, key):
    mid = (left+right)//2
    if data[mid]==key: #1
        return mid
    if left: #2
        return -1
    if data[mid]>key:
        return search(data, left, mid-1, key)
    else: return search(data, mid+1, right, key)
def f(x):
    print(search([3, 17, 19, 21, 29], 0, 5, x))
f(29)