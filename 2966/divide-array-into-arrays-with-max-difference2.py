# LeetCode 2966. Divide Array Into Arrays With Max Difference
# 將 nums 陣列「三個一組」, 希望裡面的距離 <= k。如果無法做, return []
# 
# 要把 nums[i] 分到「大小為3」 的一堆 array 裡
# 每個數「剛好用1次」，且array裡任2數的diff <= k
# 只要 return 任一種分法。但做不出來，就 return []
# 其實，只要把 nums.sort() 從小到大排好，便能開始放答案
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 != 0: return []  # 數量不對, 無法「三個一組」

        nums.sort()  # 數字小到大排好
        ans = []  # 「三個一組」依序塞到 ans 裡
        for i in range(0, len(nums), 3): # 每次挑3個 nums[i], nums[i+1], nums[i+2]
            if nums[i+2] - nums[i] > k:  # 這3個「最大減最小」超過範圍
                return [] # 就直接失敗
            ans.append(nums[i:i+3]) # 在合理範圍，就「三個一組」加入ans
        return ans
