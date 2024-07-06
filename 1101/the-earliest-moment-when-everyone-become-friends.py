# LeetCode 1101. The Earliest Moment When Everyone Become Friends
# 什麼時候大家變成朋友？logs裡，有每個人相認識的時間
# 使用 Union & Find 應該就可以解決了
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def find(a):
            if a==leader[a]: return a
            leader[a] = find(leader[a]) # 邊找邊更新
            return leader[a]
        def union(a,b):
            a, b = find(a), find(b)
            if a==b: return 0 # 早就是同一群組，用0步就完成
            leader[a] = b
            return 1 # 要再1步，才完成群組合併
        
        leader = [i for i in range(n)]
        logs.sort() # 因 logs 可能很亂，要記得sort()
        for t,a,b in logs:
            if union(a,b): # 有做結合的動作，就有1格的進展
                n -= 1 # 總共n個人，需要合併n-1次
                if n == 1: return t # 所以變成1群時，就成功了
        return -1
# case 24/67: [[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]] n=4 可能很亂，要記得 sort()

