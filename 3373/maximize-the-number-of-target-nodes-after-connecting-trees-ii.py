# LeetCode 3373. Maximize the Number of Target Nodes After Connecting Trees II
# 若 tree 有 n 個 nodes, 會有 (n-1) 條 edges。edge1 及 edge2 對應「左邊 tree1」及「右邊 tree2」
# 找出 ans 陣列，其中 ans[i] 對應「左邊tree1」的 node i 用「偶數距離」能到的最多 nodes 數量（再用1條 edge 接2個tree）
# 策略：把 tree1 和 tree2 的 nodes 依照「相鄰關係」分成偶數、奇數的不同色（偶數0、奇數1），則「同色的距離必為偶數」
# 左邊「偶數距離」的 nodes 數，是 (even1 if color1[i]==0 else odd1)。右邊可技巧性的連接，讓答案再增加最多 max(even2, odd2) 
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        path1, path2 = defaultdict(list), defaultdict(list)
        for a, b in edges1:  # 建出 path 資料結構，以便知道 a 能到哪些 nodes
            path1[a].append(b)
            path1[b].append(a)
        for a, b in edges2:
            path2[a].append(b)
            path2[b].append(a)
        N1, N2 = len(edges1)+1, len(edges2)+1  # 找出2個tree的 nodes 數量
        def helper(path, i, color, now):  # 用「函式呼叫函式」將「奇、偶」著色不同色
            color[i] = now  # 現在這個 node i 的色彩是 now
            for node in path[i]:
                if color[node]==-1:
                    helper(path, node, color, 1-now)  # 相鄰的，換另一色 1-now
            return
        color1, color2 = [-1] * N1, [-1] * N2  # 「左、右」treeh 的色彩（-1 未著色，將變 0 或 1）
        helper(path1, 0, color1, 0)  # 從 node 0 開始著色
        helper(path2, 0, color2, 0)  # 從 node 0 開始著色
        even1, even2 = color1.count(0), color2.count(0)  # color1 與 color2 裡「著色 0」的數量
        odd1, odd2 = N1 - even1, N2 - even2 # 「著色 1」的數量
        max2 = max(even2, odd2)  # tree2 裡，奇數 node、偶數 node，最多的那個，可讓答案「技巧性增加最多」
        ans = [max2 + (even1 if color1[i]==0 else odd1) for i in range(N1)]
        return ans
