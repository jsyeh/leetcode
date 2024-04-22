# 要開號碼鎖，從0000開始試，有一堆 deadends 轉到，就會卡住
# 問要轉幾次，才能轉成 target。可以使用 BFS 逐一探索
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target=="0000": return 0
        if "0000" in deadends: return -1 # 一開始就卡住，註定失敗
        # 建立 pre 跟 post 的對照表
        post = {str(i):str((i+1)%10) for i in range(10)} # 往後轉 "0":"1" ...
        pre = {post[i]:i for i in post} # 往前轉 "1":"0" ...

        visited = set() # 試過的號碼 visited 不會再試
        dead = set(deadends) # 壞掉的地方，放在 dead 裡，不能轉它
        queue = deque() # 利用 queue 進行 BFS
        queue.append(("0000", 0)) # 記錄現在的號碼 及 第幾步
        visited.add("0000") # 試過這個號碼了
        while len(queue)>0:
            now, step = queue.popleft() # 現在要處理的號碼，及對應步數
            for i in range(4): # 四個號碼，依序往後、往前轉
                next1 = now[:i] + post[now[i]] + now[i+1:] # 往後轉
                if next1 not in dead and next1 not in visited: # 可轉
                    if next1==target: return step+1 # 成功了！
                    queue.append((next1, step+1))
                    visited.add(next1)
                next2 = now[:i] + pre[now[i]] + now[i+1:] # 往前轉
                if next2 not in dead and next2 not in visited:
                    if next2==target: return step+1
                    queue.append((next2, step+1))
                    visited.add(next2)
        return -1 # 沒有成功，失敗了
# case 45/48: ["0000"], 8888
