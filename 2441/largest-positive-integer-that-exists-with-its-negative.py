# 在 nums[i] 陣列裡, 找最大的正整數, 同時它對應的負數也要在裡面。
# 陣列裡, 總共只有 1000 個數字。數字不多, 題目比較簡單。
# (1) 可先把數字排序好, 再從大到小去找。(2)也可使用 HashMap 做快速的對照表。
# 又因為數字介於 -1000到+1000間, 所以(3)也可開陣列, 把出現過的數字標示起來。
# 這裡先試著用方法(3)
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        N = len(nums)
        table = [0] * 1001  # 對應正負數。如果遇到正數,就標+1。遇到負數,就標-1
        ans = -1  # 如果沒有找到答案的數字, 預設回傳 -1
        for num in nums:  # 每個數字, 都在 table[num] 標示
            if num > 0:  # 正數
                if table[num] == 0:  # 第一次出現
                    table[num] = +1  # 就標示 +1
                elif table[num] < 0 and num > ans:  # 之前曾出現負數, 且答案更大
                    ans = num  # 就更新答案
            if num < 0:  # 負數, 等一下 table[裡面要用-num] 因為負負得正
                if table[-num] == 0:  # 第一次出現
                    table[-num] = -1  # 就標示 -1
                elif table[-num] > 0 and -num > ans:  # 之前曾出現正數, 且答案更大
                    ans = -num  # 就更新答案
        return ans
