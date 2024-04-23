# MHT 要怎麼調整樹的 root 可以讓 tree 最短：把這些可能的 root 回傳
# 因 nodes 有 2*10^4 所以不能用暴力法
# 題目的 Hint 暗示「最多有幾個答案？」
# 再觀察發現：好像就「最中間」的點，就是答案。所以最多2個答案。
# 在 Discussions 裡，有許多討論，其中一個解法是：找端點，一起刪；持續做
# 這個方法好像很容易理解，只是我擔心會不會太慢。後來看了 Solutions 裡 dietpepsi 的解法
# https://leetcode.com/problems/minimum-height-trees/solutions/76055/share-some-thoughts
# 就是用這個觀念，而且可以成功。就用這個方法吧
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0] # 如果只有1個node，都便是世界的中心
        neighbor = [set() for _ in range(n)]
        for a,b in edges: # 依照 edges 建出 neighbor 的相鄰關係
            neighbor[a].add(b)
            neighbor[b].add(a)
        # 利用迴圈，找出 len(neighbor[i])==1 的全部葉子
        leaf = [i for i in range(n) if len(neighbor[i])==1 ]
        while n > 2: # 如果目前剩的nodes 超過2個，代表還可拔葉子
            n -= len(leaf) # 葉子拔掉後，下次node就變少了
            newLeaf = [] # 一邊拔葉子，一邊「即時」算出「下次的葉子」
            for a in leaf:
                b = neighbor[a].pop() # 葉子a只有1個鄰居b
                neighbor[b].remove(a) # 拔掉b的鄰居a
                if len(neighbor[b])==1: # 拔掉後，如果b變成下一輪的葉子
                    newLeaf.append(b) 
            leaf = newLeaf # 接力，換下一輪的葉子
        return leaf # 最後剩下的 1 or 1 片葉子，便是原本的「中心」！
# case 70/71: n=1, edges=[], 
