# LeetCode 3372. Maximize the Number of Target Nodes After Connecting Trees I
# edges1 及 edges2 對應 2 組 tree 結構：n nodes 用 (n-1) edges 相連
# 你可任意挑2個點、將 tree1 tree2 接起來，希望找到最多的「夠近的點」
# u 能到 v 的距離 <= k 是夠近，問 edges1 對應 tree1 中，每個 node i 「夠近的點」的數量
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        path1 = defaultdict(list)
        for a, b in edges1:
            path1[a].append(b)
            path1[b].append(a)
        path2 = defaultdict(list)
        for a, b in edges2:
            path2[a].append(b)
            path2[b].append(a)
        def helper(path, i, k):  # path 資料結構中，第 i 點出發，距離 <=k 的數量 
            if k<0: return 0
            queue = deque()
            queue.append((0,i))  # node i 為起點
            visited = set([i])  # 走過 node i
            ans = 1 # 先把自己本身加進去
            while queue:
                d, i2 = queue.popleft()  # i2 距離 i 長度為 d2
                if d>=k: break  # 距離超過，就不要再用 for 迴圈走了
                for i3 in path[i2]:  # i2 能走到 i3
                    if i3 in visited: continue  # 走過就不要再走
                    queue.append((d+1,i3))
                    visited.add(i3)
                    ans += 1
            return ans
        N, M = len(edges1)+1, len(edges2)+1
        print([helper(path2, i, k-1) for i in range(M)])
        dist2 = max([helper(path2, i, k-1) for i in range(M)]) # 先算出 tree2 對應「距離<=k-1」的最大值
        print(dist2)
        ans = [dist2 + helper(path1, i, k) for i in range(N)]
        return ans
