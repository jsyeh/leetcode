# LeetCode 3201. Find the Maximum Length of Valid Subsequence I
# 找到最長的 valid subsequence 即「相鄰兩數」%2 都相同
# 可「左到右」依序「挑成員」加入 subsequence 即可
# 共有4種可能：湊偶數or湊奇數（二選一）、偶數開始or奇數開始（二選一）
# 每個數都%2後，就是「有幾個0」（「相鄰兩數」%2==0）「有幾個1」（「相鄰兩數」%2==0）
# 「有幾個0、1交錯」（「相鄰兩數」%2==1）
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = [num%2 for num in nums]  # 先把全部的數都%2，變成0或1，對應偶數、奇數
        ans0 = nums.count(0)  # 有幾個0（都選偶數「相鄰兩數」%2==0）
        ans1 = nums.count(1)  # 有幾個1（都選奇數「相鄰兩數」%2==0）
        ans01 = 1  # 接下來要數一下「有幾個0、1交錯」（偶數奇數交錯，「相鄰兩數」%2==1）
        for i in range(1,len(nums)):  # 每項都跟「前一項」比較
            if nums[i-1] != nums[i]: ans01 += 1  # 只要不相同，就是0、1交錯
        return max(ans0, ans1, ans01)  # 最大的答案
