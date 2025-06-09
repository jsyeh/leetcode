# LeetCode 255. Verify Preorder Sequence in Binary Search Tree
# 這題我之前是使用「函式呼叫函式」試著照 preorder 建 Binary Search Tree 
# 不過那時用的方法有點難、有點不直覺, 速度又慢。
# preorder 的性質, 是最前面的那個是 root, 後面分兩群, 都符合這樣的條件, 直到結束
# 有人使用 stack 來解, 好像也合理。我試試。
# 先有左邊界, 然後是root, 再來是比 root 大, root 又變左邊界。stack 最上面放 root
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        left = -inf # 左邊界
        for root in preorder: # 每個人這輩子, 都能當一次 root 哦 :)
            if root < left: # root 不能比左邊界小
                return False # 不合規定, 就是錯誤的 preorder
            while len(stack)>0 and root > stack[-1]: # 如果 stack 裡壓不住
                left = stack.pop() # 持續吐出之前的 root 當左邊界
            stack.append(root) # 每個人這輩子, 都能當一次 root 哦 :)
        return True # 順利解碼完畢
