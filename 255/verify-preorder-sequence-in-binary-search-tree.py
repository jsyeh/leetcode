# Input 是陣列，要把它變成 BST (Preorder Tree)
# 想到，可以用 449. Serialize and Deserialize BST 的技巧
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        def buildTree(Q: collections.deque, lo: int, hi: int):
            if len(Q)==0: return # 長度用完，就結束
            val = Q[0] # 偷看 Q[0] 
            if val<lo or val>hi: return # 不合理，就不要做
            Q.popleft() # 取出 Q[0]，也就是取出root
            # print(Q, lo, hi)
            buildTree(Q, lo, val)
            buildTree(Q, val, hi)

        Q = deque(preorder)
        buildTree(Q, -1, max(preorder)+1)
        return len(Q)==0 # 順利建完BST Tree、剩下0個，就是成功
        # 意思是，如果queue有剩，那就是失敗了

