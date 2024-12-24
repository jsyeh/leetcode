# LeetCode 3203. Find Minimum Diameter After Merging Two Trees
# 有兩組 tree（用 edges 表示）用 1 個 edge 連起來，要建出最小的 diameter 直徑（最遠兩點的距離edge數）。
# 最好的作法，是把（接近圓心）的點接起來。可用「剝葉子」的方法，找到「核心」及對應的「直徑」
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diameter(edges):  # 算出 edges 這個 tree 對應的最大直徑
            ans = 0  # tree graph 的直徑
            path = defaultdict(list)  # 相鄰 edges 的對照表
            degree = defaultdict(int)  # 某個node的「對外」連結數
            depth = defaultdict(int)  # 某個node深埋的深度
            for a, b in edges:  # 建立相鄰 edges 的對照表
                path[a].append(b)  # a 可以到 b
                path[b].append(a)  # b 可以到 a

            queue = deque()  # 利用 BFS 從外緣「葉子」慢慢剝掉
            for a in path:
                degree[a] = len(path[a])  # 「對外」連結數
                if degree[a]==1: queue.append(a)  # 若只連結1個，是葉子
            cut_leaf = set()  # 準備開始 BFS 逐一剝葉子
            while queue:
                a = queue.pop()  # 現在處理「葉子」a
                cut_leaf.add(a)  # 標注「已處理」
                for b in path[a]:  # 「葉子」a 的鄰居 b
                    degree[b] -= 1  # 因葉子a剝掉了，b 的 degree 會-1
                    if degree[b]==1: queue.append(b)  # 若降為1 b 變葉子
                    if b not in cut_leaf:  # 不是被處理過的葉子，即「深埋」裡面
                        ans = max(ans, depth[a]+depth[b]+1)  # 兩者深埋程度 半徑+半徑+1，便是直徑
                        depth[b] = max(depth[b], depth[a]+1)  # 更新 b 深埋的程度：a的半徑 + 1個edge
            return ans
        d1, d2 = diameter(edges1), diameter(edges2)  # 算出「兩團」的直徑（內部最長距徑）
        return max( d1, d2, (d1+1)//2 + (d2+1)//2 + 1 )  # 最後「直徑」有3種可能：左大（吃掉右）、右大（吃掉左）、半徑+半徑+1
