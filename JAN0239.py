def dfs(cave_id, caves, visited, current_gold):
    # 記錄目前山洞的最大黃金數量
    max_gold = current_gold
    
    # 獲取該山洞的資料
    gold, next_cave1, next_cave2 = caves[cave_id]
    
    # 更新累積黃金數量
    current_gold += gold
    # print(cave_id,[visited[next_cave1],visited[next_cave2]],current_gold)
    
    # 標記當前山洞已經走過
    visited[cave_id] = True
    
    # 如果下一個山洞是空的，則返回目前的黃金
    if( next_cave1 == 0 and next_cave2 == 0 )or (visited[next_cave1]==True and visited[next_cave2]==True):
        visited[cave_id] = False
        return current_gold
    
    # 如果沒有走過，繼續探索
    if next_cave1 != 0 and not visited[next_cave1]:
        max_gold = max(max_gold, dfs(next_cave1, caves, visited, current_gold))
    
    # 如果沒有走過，繼續探索
    if next_cave2 != 0 and not visited[next_cave2]:
        max_gold = max(max_gold, dfs(next_cave2, caves, visited, current_gold))
    
    # 完成後，標記山洞未走過
    visited[cave_id] = False
    return max_gold

def treasure_hunt(n, k, cave_info:dict):
    # 創建一個字典來存儲每個山洞的信息
    caves = {}
    for info in cave_info:
        cave_id, gold, next_cave1, next_cave2=info
        caves[cave_id] = (gold, next_cave1, next_cave2)
    
    # 記錄每個山洞是否已經被走過
    visited = [False] * (n +min(caves.keys()))
    
    # 開始從山洞k進行尋寶
    max_gold = dfs(k, caves, visited, 0)
    
    return max_gold

# 測試例子
e,f = input().split()
n=int(e)
k=int(f)
cave_info = dict()
cave_info=[[int(i) for i in input().split()]for _ in range(n)]
print(treasure_hunt(n, k, cave_info))
