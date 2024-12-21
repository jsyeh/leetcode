# LeetCode 2872. Maximum Number of K-Divisible Components
# 把 tree 斷開成很多個「小樹」，小樹的node加起來必須是 k 的倍數。最多可分成幾個「小樹」？
# Hint 1 把樹抖一抖，拿 node 0 當 root 建出「樹的樣子」，就能「函式呼叫函式」去分析
# Hint 2 從「葉子」開始往上看「能不能剪掉(k的倍數)」，不能剪掉，就和上面合併
class TreeNode:  # 自製的 tree node 資料結構（模仿 LeetCode 常見的 Tree 結構）
    def __init__(self, val=0):
        self.val = val  # TreeNode 裡的值
        self.children = []  # 可有很多 child node
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def buildTree(i):  # 建出 i 為主的樹
            tree = TreeNode(values[i])  # 以 i 建樹
            visited.add(i)  # i 用過（走過，就不會再走）
            for i2 in path[i]:  # 可走到的 node
                if i2 in visited: continue # 之前走過，就不要拿來用
                now = buildTree(i2)  # 把下一層「小樹」建出來
                tree.children.append(now)  # 加到 tree.children 裡
            return tree  # 建好「以i為主」的樹
        def helper(root, k):  # 照演算法，看 child 能不能剪掉
            if root==None: return 0  # 下面是空的，就可結束
            total = root.val  # 現在這個樹，裡面的 total 值是多少
            for child in root.children:  # 針對每個 child 
                now = helper(child, k)  # 函式呼叫函式
                if now%k==0: self.ans += 1  # 這個 child 可被剪掉，ans +1
                else: total += now  # 沒辦法剪掉，就往上加入 total
            return total  # 目前還沒被剪掉的 total 值
        path = defaultdict(list)  # 先照著 edges 結構，建出 path 資訊
        for a, b in edges:
            path[a].append(b)  # a 可以到 b
            path[b].append(a)  # b 可以到 a 
        visited = set()
        root = buildTree(0)  # 以 0 當 root 建出整個 tree
        self.ans = 0  # 目前剪掉的樹的次數
        helper(root, k)  # 慢慢去「剪掉」樹
        return self.ans + 1  # 加上沒有剪掉的主枝，總共有 self.ans + 1 個樹
