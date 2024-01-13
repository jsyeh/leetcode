# 題目給你 key 在位置 i 的地方，找出 nums[i+1] 出現最多的數是什麼
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freq = defaultdict(int)
        ans = -1 # 因為數字 1<=nums[i]<=1000 所以 -1不存在
        for i in range(len(nums)-1):
            if key==nums[i]: # 找到 key 對應的 index i
                freq[nums[i+1]] += 1 # 把 nums[i+1] 拿去統計數數
                if freq[nums[i+1]]>freq[ans]: # 出現次數更多
                    ans = nums[i+1] # 就更新 ans
        return ans
