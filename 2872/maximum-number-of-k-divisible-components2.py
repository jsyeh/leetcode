# LeetCode 2872. Maximum Number of K-Divisible Components
# 把 tree 斷開成很多個「小樹」，小樹的node加起來必須是 k 的倍數。最多可分成幾個「小樹」？
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # 看到濬帆大大「沒有」建 tree 結構，就直接算出答案，覺得很帥，所以再寫一次
        def helper(i):
            visited.add(i)  # 標示「走過」
            total = values[i]  # 目前的總合
            for i2 in path[i]:  # 針對「相鄰」的node，是不是subtree呢？
                if i2 in visited: continue  # 走過，就不要再走
                now = helper(i2)  # 函式呼叫函式
                if now%k==0: self.ans += 1  # 合乎題目要求，可以剪掉，答案+1
                else: total += now  # 無法剪掉的，合併在上面
            return total  # 這個 subtree 還沒被剪掉的 total 總合
        path = defaultdict(list)  # 先照著 edges 結構，建出 path 資訊
        for a, b in edges:  # 依照 edge 建出「相鄰路徑」的關係
            path[a].append(b)  # a 可以到 b
            path[b].append(a)  # b 可以到 a 
        visited = set()
        self.ans = 0  # 目前剪掉的樹的次數
        helper(0)
        return self.ans + 1  # 加上沒有剪掉的主枝，總共有 self.ans + 1 個樹
