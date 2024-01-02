# LeetCode 2610. Convert an Array Into a 2D Array With Conditions
# 今天的程式, 是將 Array 的內容照某種規則, 放入 2D Array
# 每個 row 裡的整數必須不同, row 越少越好。
# 其實只要先 sort(), 再把重覆的數字, 放到不同的 row 即可
# [1,3,4,1,2,3,1]
# [1,1,1,2,3,3,4]
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 先把數字排好
        ans = [ [ nums[0] ] ] # 把最前面、最小的數字, 放在兩層方括號裡
        repeat = 0 # 目前的數字 nums[0] 沒有重覆
        N = len(nums) # 有幾個數字
        for i in range(1,N): # 想比較 nums[i] vs. nums[i-1] 是否相同
            if nums[i] == nums[i-1]: # 這裡要處理, 重覆,相同, 就 repeat += 1
                repeat += 1 
                if len(ans)<=repeat: # 目前的層數不夠多
                    ans.append( [] ) # 增加一層樓
            else: # 沒有重覆
                repeat = 0 # 沒有重覆, 可以放入 ans[0] 那一層
            ans[repeat].append( nums[i] ) # 將數字 nums[i] 加到 ans[repeat]這層樓
        return ans
