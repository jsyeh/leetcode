# LeetCode 2097. Valid Arrangement of Pairs
# 「頭尾相接」全部走完
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        path = defaultdict(list)  # 所有可能的走法「a到b」
        head = Counter()  # 數一數，誰要當「開始點」（頭）
        for a,b in pairs:  # a 到 b
            path[a].append(b)  # a 可以到 b
            head[a] += 1  # a當頭的次數+1
            head[b] -= 1  # 尾與頭對消，所以 b 當頭的次數 -1
        # 先找到「開始點」，也就是「只在前面」及「只在後面」的數
        for i in head:
            if head[i]==1:
                a = i  # 確定頭在哪裡
                break  # 並離開迴圈（如果都沒找到，會用第7行殘留的a）
        ans = []
        stack = [a]  # 用 stack 實作 DFS探索，先放「開始點」
        while stack:  # 想暴力試完全部可能。如果 stack 還沒用完，就繼續
            # 處理 stack 最後一筆，當某段的起點
            while path[stack[-1]]: #while path[a]:  # 還有路能走
                # （用掉）path[stack[-1]]的下一個目的地b，放入stack
                stack.append(path[stack[-1]].pop())  # 增加新的探索點b
            b = stack.pop()  # 最後的位置
            ans.append(b)  # 全部探索完，更新ans
        # 倒過來的迴圈，把「倒過來」探索完畢的ans接出一條路徑
        return [[ans[i+1],ans[i]] for i in range(len(ans)-2,-1,-1)]
