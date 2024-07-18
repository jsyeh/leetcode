# LeetCode 1530. Number of Good Leaf Nodes Pairs
# tree 裡「兩leaf的距離<=distance」有幾組? 很像民法親屬篇的「幾等親」概念。
# 可用「函式呼叫函式」看「跨越」某個「小root」左右的深度、數量。回傳0~10深度葉子的數量
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        def find(root):  # 要計算「所有左邊leaf深度」及「所有右邊leaf深度，更新答案
            if root==None: return [0]*10  # 空的、什麼都沒有
            if root.left==None and root.right==None: 
                return [0,1,0,0,0,0,0,0,0,0]  # 左右空，即1片(深度為1的)葉子
            a1 = find(root.left) # 找出 a1[0]..a1[9]
            a2 = find(root.right) # 找出 a2[0]..a2[9]
            for i in range(10):
                for j in range(10):
                    if i+j<=distance: # 最高點「跨過root」的合理深度（本層左右都+1）
                        self.ans += a1[i]*a2[j] # 即把左邊、右邊的排列組合 加起來
            return [0] + [a1[i]+a2[i] for i in range(9)] # 深度再加1層
        find(root) # 好好的算答案
        return self.ans
