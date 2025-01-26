# LeetCode 2127. Maximum Employees to Be Invited to a Meeting
# 在圓桌「邀請員工」入座，但favorite[i]代表員工i「想坐在(某人)旁邊」，最多圓桌裡會坐幾人？
# 每人只堅持找「另一人」，graph不會太複雜。但我有點卡住，所以參考 Solutions 裡 Vlad 的巧妙解法：
# (1) 兩個員工互相喜歡時，可簡單坐在一起（小鑰匙圈，配許多小鏈是合法的）。其他喜歡的，可以慢慢加長。把這些鏈狀「全加起來」，or
# (2) 找最大的 cycle loop (a喜歡b,b喜歡c,繞一大圈，喜歡a)（大鑰匙圈，只能看大圈圈）。再(1)(2)比誰大即可
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N = len(favorite)  # 有 N 位員工 0...N-1，每位員工「只愛1人」。每人有2種可能：可能是「單戀/單鏈」、可能是cycle
        graph = defaultdict(list) # Hint 1 建議「轉成 graph 問題」
        # Hint 2: 若挑 graph 裡的1個大cycle（大鑰匙圈），那其他人就不能再坐進來，以免破壞cycle
        # Hint 3: 若不挑大 cycle，就把一堆chains併在一起（許多小鑰匙圈+單鏈，可利用 BFS/DFS 把全部的 cycles 和 chains 找出來，再挑即可
        for i in range(N):  # graph[i] 方便 DFS 找最長的 chain
            if favorite[favorite[i]] == i: continue  # 避開「互相喜歡的2人」（最小的cycle/小鑰匙圈），將生長出「單鏈」
            graph[favorite[i]].append(i)  #  graph[i] 代表「喜歡i的人」有誰，可建出許多「單戀/單鏈」的結構
        def checkChainLen(i):  # graph[i] 方便
            maxLen = 0  # DFS 找到（從i出發）最長的單鏈 chain 的長度
            for ii in graph[i]:
                maxLen = max(maxLen, checkChainLen(ii))
            return maxLen + 1  # 喜歡 i 的「最長chain」有多長
        ans = 0  # (1) 現在開始收集「能上桌」的答案
        for i in range(N):  # 首先，先從「互相喜歡的2人」的小鑰匙圈出發，收集「各自最長的單戀/單鏈」
            if favorite[favorite[i]] == i:  # 遇到「互相喜歡的2人」，可當「某個chain開頭」
                ans += checkChainLen(i)
        # (2) 最後，嘗試找最長的 cycle（這裡我模仿 Solutions 裡 Bakerston 的解法）
        seen = [False] * N  # 一開始，都還沒測試過、還沒看過
        for i in range(N):  # 依序處理
            if not seen[i]:  # 若 node i 沒看過，便能進行 cycle loop test
                start = i  # 先備份「起始點」
                cur_people = i  # 從起始點出發的人
                visited = set()  # 走過，代表「遇到cycle」，就不再走
                while not seen[cur_people]:  # 照著 a喜歡b，b喜歡c，c喜歡d，這樣一直走，直到「走過了」
                    seen[cur_people] = True  # 標示「這格走過了」
                    visited.add(cur_people)  # 在 這輪「參與過的人」，會與 cycle loop 大小有關
                    cur_people = favorite[cur_people]  # 照著 a喜歡b，b喜歡c，c喜歡d，這樣一直順著走
                if cur_people in visited:  # 若撞到、有cycle發生
                    cycleSize = len(visited)  # 這趟有走過的人，將要「扣掉」前面「不是loop」的部分
                    while start != cur_people:  # 出發點「也做一次」直到「也撞到」剛剛「發生loop」碰撞點
                        cycleSize -= 1  # 還沒碰到「碰撞點」，這個長度要扣掉，因為「還沒進入 loop 本體
                        start = favorite[start]  # 下一格
                    ans = max(ans, cycleSize)  # 若 cycle loop 更大，更新答案
        return ans
