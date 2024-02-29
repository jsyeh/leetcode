# 確認某個 binary tree 是不是 even-odd tree
# 也就是在 even 層, 數字都要是 odd 且嚴格遞增
# 在 odd 層, 數字都是 even 且嚴格遞減
# 有 10^5 個 nodes 還蠻多的。我想到可以用 queue 進行 BFS 並確認是否合格
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((root, 0)) # 先把 (root,level 0) 加入 queue 裡
        levelValue = [] # 用來存 level i 的 levelValue[i] 以便檢查 嚴格遞增or遞減
        while len(queue)>0: # 持續進行 BFS
            node, level = queue.popleft() # 取出, 逐一檢查
            if level%2==0 and node.val%2==0: return False # 失敗
            if level%2==1 and node.val%2==1: return False # 失敗
            
            if len(levelValue)<=level: # 層數不夠, 加新的一層
                levelValue.append(node.val) # 本層「最左邊」的第1個數字
            else: # 要檢查「嚴格遞增」or「嚴格遞減」
                if level%2==0 and levelValue[level]<node.val: # 符合嚴格遞增
                    levelValue[level] = node.val # 更新
                elif level%2==1 and levelValue[level]>node.val: # 符合嚴格遞減
                    levelValue[level] = node.val # 更新
                else: # 不符合
                    return False 
            if node.left!=None: queue.append((node.left, level+1)) # 加入下一層
            if node.right!=None: queue.append((node.right, level+1)) # 加入下一層
        return True # 都沒有「不符合」,順利完成
