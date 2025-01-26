class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N = len(favorite)  # 總共 N 個人
        following = defaultdict(list)  # graph[k] 有哪些人暗戀k
        for i in range(N):  # 做出 N 人暗戀對照表
            if favorite[favorite[i]] == i: continue  # 兩人互相喜歡，就不叫暗戀
            following[favorite[i]].append(i)
        def findChainLen(i):  # 用「函式呼叫函式」找「單戀/單鏈」的長度
            maxLen = 0
            for ii in following[i]:  # 一堆 ii 喜歡 i
                maxLen = max(maxLen, findChainLen(ii))
            return maxLen + 1
        ans = 0  # 累積「2人小圈」的單鏈長度
        for i in range(N):
            if favorite[favorite[i]]==i:
                ans += findChainLen(i)  # 累積「2人小圈」的單鏈長度
        seen = [False]*N  # 接下來，處理「cycle loop」大圈圈的部分
        for i in range(N):
            if not seen[i]:  # 還沒試過的，試試看
                visited = set()
                user1, user2 = i, i  # 兩個人，分別都將從「起點i」出發
                while not seen[user1]:  # 用 while 迴圈，嘗試「繞圈圈」
                    seen[user1] = True
                    visited.add(user1)
                    user1 = favorite[user1]
                if user1 not in visited: continue  # 最後沒能繞圈圈，放棄這輪
                cycleLen = len(visited)  # 要判斷 cycle loop 圈圈的大小（第1個人已站在圈圈入口）
                while user2 != user1:  # 「第2人」要去追「第1人」，追到之前，距離都要扣掉
                    cycleLen -= 1  # 追到之前，距離都要扣掉
                    user2 = favorite[user2]  # 往前走
            ans = max(ans, cycleLen)
        return ans
