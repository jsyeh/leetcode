# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # 技巧：每次挑1個數，當中間的root。再函式呼叫函式後，再把 Tree 組合起來
        def buildSubTree(nums: List[int]) -> List[Optional[TreeNode]]:
            if len(nums) == 0: return []
            if len(nums) == 1: return [TreeNode(nums[0])]

            ans = []
            for i in range(len(nums)):
                lefts = buildSubTree(nums[:i])
                rights = buildSubTree(nums[i+1:])
                for left in lefts: # 這個迴圈有點可惜，因空集合就不會做事
                    for right in rights:
                        tree = TreeNode(nums[i], left, right)
                        ans.append(tree)
                if lefts == [] and rights != []: # 因前面迴圈無法做到，所以補做
                    for right in rights:
                        tree = TreeNode(nums[i], None, right)
                        ans.append(tree)
                if rights == [] and left != []: # 因前面迴圈無法做到，所以補做
                    for left in lefts:
                        tree = TreeNode(nums[i], left, None)
                        ans.append(tree)
            return ans
        
        nums = [i for i in range(1,n+1)]
        # print(a) # 發現這種建list當陣列的方法又帥又簡潔
        return buildSubTree(nums)

