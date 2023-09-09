# 要找出排列組合的全部可能數目，可以利用「函式呼叫函式」的top-down DP來完成
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def helper(target: int) -> int:
            if target==0: return 1

            ans = 0
            for n in nums:
                if target-n>=0: ans += helper(target-n)
            return ans

        return helper(target)
