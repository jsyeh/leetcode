class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        tail = 0
        M = max(nums) # 找最大值
        MN = 0 # 最大值出現幾次呢?
        for head in range(len(nums)): # 以頭為準, 慢慢往右吃
            if nums[head]==M: MN += 1 # 找到最大值, 多一次
            # 目標: 希望 MN >=k 合法
            while MN>=k:
                # 尾巴一直縮, 直到不合法為止, 因為剛好對應答案
                if nums[tail]==M: MN -= 1 # 少掉一個
                tail += 1 # 尾巴往右縮
            # 縮完之後, tail 對應左邊有幾個合法的尾巴位置
            ans += tail # 可以增加這麼多種合法的可能
        return ans
