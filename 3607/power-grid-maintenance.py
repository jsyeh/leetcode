# LeetCode 3607. Power Grid Maintenance  # 某電廠可能會關機，問同一個「電廠集團」裡，由代碼最小的電廠來供電
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        path = defaultdict(list)  # 電廠間的連結關係
        for a,b in connections:
            path[a].append(b)  # a 有連到 b
            path[b].append(a)  # b 有連到 a
        leader = [0] * (c+1)  # leader[a] 會記錄 a 所屬集團的 Leader L
        def helper(a, L):  # 設定 a 的集團 leader 是 L
            if leader[a]>0: return  # 早就找過對應的 Leader、不用再問了
            leader[a] = L  # 電廠 a 的 Leader 是 L
            for b in path[a]:
                helper(b, L)  # 函式呼叫函式，找到全部的集團成員
        for i in range(1,c+1):  # 從小到大
            helper(i, i)  # 最小的數開始，嘗試讓自己當自己的 leader
        group = defaultdict(list)  # 每個 Leader 帶領的集團 group 成員，將大到小排好
        for i in range(c, 0, -1):  # 從大到小，找每個電廠的 Leader
            L = leader[i]  # 找每個電廠的 Leader
            group[L].append(i)  # 這個 Leader 帶領的集團裡，從大到小「塞成員」
        online = [True] * (c+1)  # 電廠的開機狀態
        ans = []  # 放答案，把每次 queries 的 state 是 1 的，都要塞1個答案
        for state, x in queries:
            if state == 1:  # 要查詢「電廠x」的集團供電電廠，放入 ans 裡
                if online[x]: ans.append(x)  # 有開機，直接回傳本身
                else:  # x 關機的話，要找到「集團」裡，開機中、代號最小的電廠
                    L = leader[x]  # 先找到 Leader L，以便找 group[L] 的資訊
                    while len(group[L])>0 and not online[group[L][-1]]:  # 關機中
                        group[L].pop()  # 踢掉，集團裡不要再考慮它了
                    if len(group[L])==0: ans.append(-1)  # 集團裡「沒任何開機的電廠」
                    else: ans.append(group[L][-1])  # 集團裡「最右邊」代碼最小的電廠
            if state == 2:  # 要將電廠關機
                online[x] = False  # 關機
        return ans
