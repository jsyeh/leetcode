# LeetCode 684. Redundant Connection
# n nodes, 標成 1..n，基本上只要 n-1 個 edges 就能連起來。
# 但給 n 個 edges 所以會有 1 個 edge 是可拔除的。把它找出來。
# 但使用 DFS 跑起來蠻慢的，有更快的作法嗎？有人分享「可用 union-find」的技巧
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 想像有 N 個獨立國家要結盟：只要 N-1 次結盟，就可以了，因為每次是把「兩個不同聯盟」合併。
        # 所以「如果現在要結盟」的兩個國家「已經是同一聯盟」，這個「結盟」就是多餘的。
        N = len(edges)
        group = [i for i in range(N+1)]  # 題目是 1-index 所以要再加1個
        def find(x):  # 想知道 x 是哪一個聯盟
            if group[x]==x: return x  # 如果自己是自己的主人，那就是自己一國
            ans = find(group[x])  # 主人的主人
            if group[x] != ans:  # 繞口令：如果主人與主人的主人不同
                group[x] = ans  # 就讓「主人的主人」當成你的「主人」
            return group[x]
        for a,b in edges:  # 現在 a 和 b 想要「結盟」
            a2, b2 = find(a), find(b)  # 它們各自的主人，分別是
            if a2 == b2:  # 主人相同，是同聯盟的。「再結盟」就是「多餘的」
                return [a,b]  # 就找到答案了
            group[a2] = group[b2]  # 結盟後，大家有共同的主人哦！
