def data():
    """收集輸入數據"""
    n = inputs(0)  # 總數
    m = inputs(0)  # 迭代次數
    a = inputs(0)  # 其他參數 a
    b = inputs(1)  # 浮點數參數 b
    c = inputs(0)  # 迴圈控制參數 c
    d = inputs(1)  # 浮點數參數 d
    return n, m, a, b, c, d

def inputs(input_type):
    """根據類型輸入數據"""
    if input_type == 0:
        return int(input("請輸入整數："))
    else:
        return float(input("請輸入浮點數："))

def lab(n, m, a, b, c, d):
    """核心計算邏輯"""
    lilab = [[0, 0, 0, 0]]  # 初始狀態

    for i in range(m):
        # 避免 c 為 0 導致的錯誤
        if c == 0:
            print("參數 c 不可為 0")
            return
        
        x = int((b / c) * (1 - d))  # 計算 x
        y = lilab[i][1] * x  # 基於上一項的值計算 y
        
        if i == 0:
            # 初始情況
            lilab.append([i + 1, lilab[i][1] + y, y, 0])
        elif lilab[i][1] + y >= n * (1 - d):
            # 當累積值超過限制
            if i <= c:
                lilab.append([i + 1, n * (1 - d), n * (1 - d) - lilab[i][1], 0])
            else:
                lilab.append([i + 1, n * (1 - d) - lilab[i - c][1], 0, lilab[i - c][1]])
                d += lilab[i - c][1] / n
        else:
            # 常規情況
            if i <= c:
                lilab.append([i, lilab[i][1] + y, y, 0])
            else:
                lilab.append([i, lilab[i][1] + y - lilab[i - c][1], y, lilab[i - c][1]])
                d += lilab[i - c][1] / n

    # 返回結果
    return lilab

def main():
    # 收集輸入
    n, m, a, b, c, d = data()
    # 執行核心計算
    result = lab(n, m, a, b, c, d)

    # 輸出結果
    if result:
        print("計算結果：")
        for row in result:
            print(row)

# 執行主程式
main()
