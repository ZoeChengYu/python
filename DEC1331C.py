def intdata():
    data = input().split()
    for i in range(len(data)):
        if 'a' <= data[i] <= 'f':
            data[i] = 10 + (ord(data[i]) - ord('a'))
        elif 'A' <= data[i] <= 'F':
            data[i] = 10 + (ord(data[i]) - ord('A'))
        else:
            data[i] = int(data[i])
    return data

def math(data):
    permutations = []
    from itertools import permutations as perm
    hex_permutations = perm(data)
    for p in hex_permutations:
        value = 0
        for digit in p:
            value = value * 16 + digit
        permutations.append(value)

    permutations.sort()
    big = permutations[-1]
    small = permutations[0]
    mid_index = len(permutations) // 2
    if len(permutations) % 2 == 0:
        mid = (permutations[mid_index - 1] + permutations[mid_index]) // 2
    else:
        mid = permutations[mid_index]
    
    return big + small + mid

def outline(sum):
    if sum < 10:
        print(sum)
    else:
        return outline(sum // 10 + sum % 10)

def main():
    data = intdata()
    sum = math(data)
    outline(sum)

main()
