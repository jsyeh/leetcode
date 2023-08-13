# 用 Testcase測試 [-1,1] k=0 它的答案是2，不會是0
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # 可以把 nums[i] 改成 running sum
        # 有了 running sum, 便能用hashmap快速知道 k 的反數
        N = len(nums)
        table = {}
        table[0] = -1 # 最原始的距離，在陣列外面
        # table[nums[0]] = 0 # 會蓋到 table[0] = -1 因 case 35/36 
        ans = 0 
        if nums[0] == k: ans = 1 # 最基礎那筆 case 33/36
        for i in range(N):
            # 下面 running sum 稍修改
            if i>0: nums[i] += nums[i-1] # running sum
            target = nums[i]-k # 因 nums[i]-target = k
            if target in table: # 有幸找到target
                dist = i - table[target] # 距離i-前位置
                if dist>ans: ans = dist # 變更大的距離
            if nums[i] not in table: # 此running sum未被存過
                table[nums[i]] = i # 就記下位置
        # print(nums)
        # print(table)
        return ans
# case 33/36: [-1] -1 # 啊，我漏算了nums[0]
# case 35/36: [0,0] 0 # 啊，不能隨便加 table[nums[0]]=0
