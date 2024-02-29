# 「挑個數值(比最小值小)」減掉全部的正數
# 問要做幾次, 才能把 nums 都變成0
# 其實等價於: 總共有幾個「不同」的正數
# 如果使用 Counter 好像更容易
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter(nums) # 統計每個數出現的次數
        ans = len(counter) # 有幾個不同的數
        if counter[0]>0: ans -= 1 # 遇到0要另外處理, 因為0不能算
        return ans
