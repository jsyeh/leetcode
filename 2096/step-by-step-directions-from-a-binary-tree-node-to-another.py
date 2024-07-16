# LeetCode 2096. Step-By-Step Directions From a Binary Tree Node to Another
# 要在 Binary Tree 裡，從 A 走到 B 的走法。其實就是「先找到共同的root」再往下走即可。
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(root, node):
            if root==None: return False  # 終止條件：沒找到
            if root.val==node: return True  # 終止條件：找到
            self.path.append('L')  # 探索左半樹
            if find(root.left, node): return True
            self.path.pop()
            self.path.append('R')  # 探索右半樹
            if find(root.right, node): return True
            self.path.pop()
            return False
        self.path = []
        find(root, startValue)  # 找到的 path 要存在 self.path0
        self.path, self.path0 = [], self.path
        find(root, destValue)  # 找到的 path 會存在 self.path
        ans = []
        print(self.path0, self.path)
        L0, L = len(self.path0), len(self.path)
        for i in range(max(L0, L)):
            if i>=L0 or i>=L or self.path0[i]!=self.path[i]: # 不相同時，便結束「共同」的部分
                for k in range(i, L0): ans.append('U')  # 往上爬
                for k in range(i, L): ans.append(self.path[k]) # 往目的地走
                break
        return ''.join(ans)

