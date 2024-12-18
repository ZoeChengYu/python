def inputer():
    base = int(input())  # N 矩陣大小
    ball = int(input())  # M 被圈選的數字數量
    seto = []

    for _ in range(2):
        seto.append(bouns(base))
    
    ssd = input().split()  # 被圈選的數字
    return base, seto, ssd

def bouns(base):
    iso = input().split()  # 讀取矩陣的數字
    vol = [['0' for _ in range(base)] for _ in range(base)]  # 初始化矩陣

    for i in range(base):
        for j in range(base):
            vol[i][j] = iso[i * base + j]
    return vol

def linecount(matrix, marked):
    def is_complete_line(line):
        return all(num in marked for num in line)

    size = len(matrix)
    lines = 0
    
    # 檢查行和列
    for i in range(size):
        if is_complete_line(matrix[i]):  # 檢查行
            lines += 1
        if is_complete_line([matrix[j][i] for j in range(size)]):  # 檢查列
            lines += 1

    # 檢查兩條對角線
    if is_complete_line([matrix[i][i] for i in range(size)]):  # 從左上到右下
        lines += 1
    if is_complete_line([matrix[i][size - i - 1] for i in range(size)]):  # 從右上到左下
        lines += 1

    return lines

def main():
    base, data, lists = inputer()
    
    line = [0, 0]
    for i in range(2):
        line[i] = linecount(data[i], lists)
    
    if line[0] > line[1]:
        print('A Win')
    elif line[1] > line[0]:
        print('B Win')
    else:
        print('Tie')

main()
