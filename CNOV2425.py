def inputs():
    # 接收輸入
    N = int(input())
    Lv = int(input())
    poka = [input() for i in range(N)]
    return poka, Lv, N

def find_keyword(data):
    # 驗證括號是否平衡
    up = ['(', '[', '{']
    down = [')', ']', '}']
    stable = []

    for char in data:
        if char in up:
            stable.append(char)
        elif char in down:
            if stable and ((char == ')' and stable[-1] == '(') or
                           (char == ']' and stable[-1] == '[') or
                           (char == '}' and stable[-1] == '{')):
                stable.pop()
            else:
                stable.append(char)

    return stable  # 返回未平衡的括號清單

def find_answer(data, Lv):
    # 提取特定層級的內容
    result = ''
    uper = ['(', '[', '{']
    down = [')', ']', '}']
    current_level = 0

    for char in data:
        if char in uper:
            current_level += 1
        elif char in down:
            current_level -= 1
        elif current_level == Lv:
            result += char

    if result == '':
        print('EMPTY')
    else:
        print(result)

def main():
    data, Lv, N = inputs()
    for i in range(N):
        # 驗證輸入條件
        if 1 <= N <= 3 and 1 <= len(data[i]) <= 50 and 1 <= Lv <= 6:
            unmatched = find_keyword(data[i])  # 檢查括號是否平衡
            if unmatched:
                print('fail')
            else:
                print('pass', end=',')
                find_answer(data[i], Lv)
        else:
            print('fail')

if __name__ == "__main__":
    main()
