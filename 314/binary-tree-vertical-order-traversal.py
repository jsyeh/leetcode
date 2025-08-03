# LeetCode 314. Binary Tree Vertical Order Traversal
# 給你 Binary Tree 請照著左右空間的分配，變成許多「直行」的內容
# 我本來使用「函式呼叫函式」即 DFS 結果「直行的順序不對」
# 後來看了 Stefan Pachmann 的解法，改用 BFS 配合 queue 完成
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)  # 改成先用字典，再對應直條
        queue = deque()  # 利用 queue 進行 BFS，便能「上到下」依序處理
        if root: queue.append((root, 0))  # 先把 root node 當成最上面的開始點
        while queue:  # 利用 queue 資料結構，依序 BFS 展開
            node, i = queue.popleft()
            cols[i].append(node.val)  # 對應 index 那條，塞入 val
            if node.left: queue.append((node.left, i-1))  # 左邊有，就塞
            if node.right: queue.append((node.right, i+1))  # 右邊有，就塞
        return [cols[i] for i in sorted(cols)]  # 照順序「左到右」組出 list 答案

        '''  # 下面方法會出錯，因「函式呼叫函式」是DFS左邊優先，而讓順序出錯
        left = []  # 座標用負的來想像，即 -1, -2, -3 慢慢過去，之後再合併
        right = []  # 座標往右 0, 1, 2, 3 增加
        def helper(root, i):  # 利用「函式呼叫函式」將 val 塞入 left 或 right
            if root==None: return
            if i<0:
                if len(left) < -i: left.append([])  # 數量不夠，再加1條
                left[-i-1].append(root.val)
            else:
                if len(right)<=i: right.append([])  # 數量不夠，再加1條
                right[i].append(root.val)
            helper(root.left, i-1)  # 「函式呼叫函式」
            helper(root.right, i+1)  # 「函式呼叫函式」
        helper(root, 0)  # 開始「函式呼叫函式」
        return list(reversed(left)) + right
        '''
