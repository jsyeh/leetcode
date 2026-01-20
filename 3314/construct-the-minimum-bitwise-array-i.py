# LeetCode 3314. Construct the Minimum Bitwise Array I
# nums 有 n 個質數，要找到 ans 陣列，使得 nums[i] = ans[i] OR (ans[i]+1)
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:  # 針對每個質數
            for i in range(num):  # 依序測試、找答案
                if num == i | (i+1):  # 若找到答案
                    ans.append(i)  # 填入答案
                    break  # 離開迴圈
            else: ans.append(-1)  # 找不到答案，填入-1
        return ans
