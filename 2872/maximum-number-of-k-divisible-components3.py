# LeetCode 2872. Maximum Number of K-Divisible Components
# 由 n nodes 及 n-1 edges 構成的 tree，每個 node 對應 values[i]
# 想辦法斷開 tree 變成最多個分開的「小樹」 裡面每個「小數」的和都是 k 的倍數。
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        path = defaultdict(list)  # 先建出 path 資料結構
        for a,b in edges:  # a,b 之間存在 edge
            path[a].append(b)  # a 可以到 b
            path[b].append(a)  # b 可以到 a

        visited = set()  # 走過的地方，不要再走
        self.ans = 1  # 累積的「小樹」有幾個？本來就一大坨，接下來 helper()砍樹
        def helper(i):  # 利用「函式呼叫函式」處理全部的點
            visited.add(i)  # 標示「走過」
            total = values[i]  # 目前的總合
            for i2 in path[i]:  # 針對「相鄰」的node，是不是subtree呢？
                if i2 in visited: continue  # 走過，就不要再走
                now = helper(i2)  # 函式呼叫函式，看小樹裡累積的 total 值是多少
                if now%k==0: self.ans += 1  # 合乎題目要求，可以剪掉，答案+1
                else: total += now  # 無法剪掉的，合併在上面
            return total  # 這個 subtree 還沒被剪掉的 total 總合

        helper(0)  # 「函式呼叫函式」，從 node 0 開始試走
        return self.ans  # 累積的「小樹」有幾個
