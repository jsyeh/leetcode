# LeetCode 3507. Minimum Pair Removal to Sort Array I
# 每次挑2個相鄰「加起來最小」換成1個數（總和），幾次後會排序好？
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if len(nums)==1: return 0  # 只有1個數，不用再處理、結束

        for step in range(len(nums)-1):  # 迴圈一步步，慢慢模擬
            bad = False  # 一開始「沒壞」
            minI, minSum = 0, nums[0]+nums[1]
            for i in range(len(nums)-1):  # 左到右，兩兩相鄰比較
                if nums[i]>nums[i+1]: bad = True  # 如果大小順序不對，壞掉
                if nums[i]+nums[i+1] < minSum:  # 如果「相鄰加起來」更小
                    minI, minSum = i, nums[i]+nums[i+1]  # 就更新
            if not bad:  # 一直都「沒壞」大小順序都對，離開
                return step
            # 下面要處理，step將再加1步
            nums[minI] = minSum  # 換成1個數（總和）
            del nums[minI+1]  # 把另一個數刪掉（這行要小心、會沒效率）
        return step + 1  # 前面處理完，還沒找到答案，step加1步
