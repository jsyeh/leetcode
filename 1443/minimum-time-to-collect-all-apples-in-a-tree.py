# LeetCode 1443. Minimum Time to Collect All Apples in a Tree
# 以 edges 表示樹（0...n-1）從樹根 0 開始，把樹上 apple 都收完，要走幾步
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        path = defaultdict(list)
        for a, b in edges:  # 先建立 path 關係
            path[a].append(b)
            path[b].append(a)

        visited = set()  # 走過，就不要再走
        def helper(a):  # 測「有幾個apple」及「要走幾步」
            if a in visited: return False, 0  # 走過，就不要再走
            visited.add(a)  # 走過，就不要再走
            apple, ans = 0, 0  # 以下「有幾個apple」及「要走幾步」
            for b in path[a]:  # 每個分支，都做分析
                apple1, ans1 = helper(b)  # 此分支「有幾個apple」及「要走幾步」
                if apple1:  # 如果有 apple，就要更新答案
                    ans += ans1 + 2  # 一去一回，走2步
                    apple += apple1
            if hasApple[a]: apple += 1  # 本身有apple也更新
            return apple, ans  # 「有幾個apple」及「要走幾步」
        apple, ans = helper(0)  # 從 root 0 開始測試、分析
        return ans
