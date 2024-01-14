# 要收集 1..k 的數：每次可從「最後」「抽出」1個數，要「抽幾次」才能湊齊1..k
# k<=50, 所以直覺暴力做，就可以了
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        bag = set() # 目前「收藏袋」收到哪些數字
        for t in range(1,51): # 逐次抽數字, 現在是第t次哦
            now = nums.pop()
            if now not in bag and now<=k: # now 還沒抽過，且沒在bag裡出現
                bag.add(now) # 放入「收藏袋」裡
                if len(bag)==k: return t # 收集完整，太棒了！
