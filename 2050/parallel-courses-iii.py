# 看起來可能是 topology sort 的題目，不過看了Editorial的解法1，覺得超簡單，就用這個解法
# 它的想法是，如果不需要再等其他課要先修的話，那門課的max_time[i]就是精準的，可以放到queue裡面
# 因為 queue裡面的 max_time[i]都是正確的，便能照著這個值，去更新它的後面課程的 max_time[next]
# 如果後面課程 next 的 indegree[next]減到變成0 代表它又是不用等其他課程了，是精準的 max_time[next]
# 就再把 next 加到 queue裡面
# 最後做完，找 max_time 陣列裡的最大值，便是全部需要的時間
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        next = {}
        indegree = [0]*(n+1) # 因為 relations 是 1-index 從1開始，所以要再加1個
        for a,b in relations: # 1-index從1開始，但time[i]是從0開始
            if a in next:
                next[a].append(b)
            else:
                next[a] = [b]
            indegree[b] += 1
        # 前面建好了 next[a] 及 indegree[b]
        # 現在要檢查 indegree[b] 如果是0的話，加到 queue裡面
        queue = deque()
        max_time = [0]*(n+1)
        time.insert(0, 0) # 為了讓 0-index 的 time[i] 變成 1-index 所以在最前面插入個數字
        for b in range(1,n+1): # 因為堅持要 1-index 哈哈哈
            if indegree[b]==0: # 沒有人會到 b 那 b 就是 root 源頭
                queue.append(b) # 加到乾淨的 queue 裡面
                max_time[b] = time[b] # 時間 time[b] 就是要完成 b 的時間，因為前面不用等別人
        
        # 最後在 queue 的迴圈裡，逐一更新後面的人
        while len(queue)>0:
            a = queue.pop()
            if a not in next: continue
            for b in next[a]:
                max_time[b] = max(max_time[b], max_time[a] + time[b])
                indegree[b] -= 1
                if indegree[b] == 0: # 乾淨了、不用等別人了，便能加入 queue
                    queue.append(b)

        return max(max_time)


        return 0

        
