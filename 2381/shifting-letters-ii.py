# shifts[i] 有 start[i], end[i], direction[i]
# direction[i] = 1 表示「增加」， direction = 0 表示「減少」
# 但因為len(s)太大 5*10^4 不能用暴力法
# 可以用 sort 把 shifts 排好，進入時，再利用 heap 把「結束」也準備好
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        heapStart = shifts
        heapify(heapStart) 
        heapEnd = []
        change = 0 # 改變量
        ans = []
        for i in range(len(s)): # 每格逐格更新
            # 先看 start 開始點，有沒有撞到
            while heapStart and heapStart[0][0]==i: # 撞到了，要取出
                # 把結束、方向，都存入 heapEnd
                heappush(heapEnd, (heapStart[0][1], heapStart[0][2]))
                if heapStart[0][2]==0: change -= 1
                else: change += 1 # 往上增 or 往下走
                heappop(heapStart) # 用完了，丟掉

            # 更新 ans[i] 的值
            now = (ord(s[i]) - ord('a') + change + 26) % 26 # 物極必反
            ans.append( chr(ord('a')+now) )
            
            # 結束時，再看 end 結束點，有沒有撞到 (這樣就能「左右都包含」)
            while heapEnd and heapEnd[0][0]==i: # 撞到了，要取出
                if heapEnd[0][1]==0: change += 1 # 反過來（還原）
                else: change -= 1 # 反過來（還原）
                heappop(heapEnd)

        return ''.join(ans)
