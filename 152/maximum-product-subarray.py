class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        table = [0]*N # table[i] 包含 nums[i] 的最大乘積
        table2 = [0]*N # table2[i] 包含 nums[i] 的最小乘積

        table[0] = nums[0] # 因為包含 nums[0] 只能是它了
        table2[0] = nums[0] # 因為包含 nums[0] 只能是它了

        ans = table[0] # 答案就先是它了
        for i in range(1,N): # 後面也是逐一巡
            if nums[i]==0: # 0 會把乘積全部變0
                table[i] = 0
                table2[i] = 0
            if nums[i]<0: # 負數，具有㒹倒逆轉的效果
                table[i] = max(nums[i], table2[i-1] * nums[i])
                table2[i] = min(nums[i], table[i-1] * nums[i])
            if nums[i]>0: # 正數，就繼續乘起來
                table[i] = max(nums[i], table[i-1] * nums[i])
                table2[i] = min(nums[i], table2[i-1] * nums[i])
            # 前面會多個 nums[i] 是擔心如果為前為0時，可能需要新的開始

            if table[i] > ans: # 關於最大的答案，順便更新一下
                ans = table[i]
        # print(table) # 在 debug 時，順手印很方便
        # print(table2)
        return ans
# case 111/190: [0,2]
