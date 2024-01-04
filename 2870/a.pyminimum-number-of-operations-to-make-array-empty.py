# 操作1: 挑2個相同的, 一起刪掉
# 操作2: 挑3個相同的, 一起刪掉
# 問最少要操作幾次, 才能把全部都刪掉
# 一樣, 先 sort()後, 再三三刪, 但剩一個時, 回成兩兩刪
# 無法刪,就結束
# 但有了 defaultdict() 的話,就不需要 sort() 了
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums: # 先統計「每個數字出現幾次」
            count[n] += 1
        # 接下來, 看字典裡的「出現數字」有幾個
        counts = list(count.values()) # 直接拿數值(出現次數)來算
        ans = 0
        for c in counts:
            if c==1: return -1 # 無法刪掉的孤單一個
            elif c%3==0: ans += c//3
            elif c%3==1: ans += c//3 + 1 # 最後4個用二二刪即可
            elif c%3==2: ans += c//3 + 1 # 最後2個用二刪掉可
        return ans
