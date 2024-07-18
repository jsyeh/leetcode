# LeetCode 1530. Number of Good Leaf Nodes Pairs
# tree 裡「兩leaf的距離<=distance」有幾組? 很像民法親屬篇的「幾等親」概念。
# 可用「函式呼叫函式」看「跨越」某個「小root」左右的深度、數量。回傳0~10深度葉子的數量
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        def find(root):  # 要計算「所有左邊leaf深度」及「所有右邊leaf深度，更新答案
            if root==None: return [0]*10  # 空的、什麼都沒有
            if root.left==None and root.right==None: 
                return {1:1}  # 左右空，即1片(深度為1的)葉子
            a1 = find(root.left)  # 找出 a1[0]..a1[9]
            a2 = find(root.right)  # 找出 a2[0]..a2[9]
            for d1 in a1:
                for d2 in a2:
                    if d1+d2<=distance:  # 最高點「跨過root」的合理深度
                        self.ans += a1[d1]*a2[d2]  # 即把左邊、右邊的排列組合 加起來
            new_depth = defaultdict(int)
            for d in range(10):
                if d in a1: new_depth[d+1] += a1[d] # 深度再加1層
                if d in a2: new_depth[d+1] += a2[d] # 深度再加1層
            return new_depth
        find(root) # 好好的算答案
        return self.ans
