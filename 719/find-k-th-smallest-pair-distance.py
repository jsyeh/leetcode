# LeetCode 719. Find K-th Smallest Pair Distance
# 找到第k組最短的距離。但 10^4 個數，暴力試全部組合 10^8 會超時
# 在題目下方 Hint 1 提示「可使用 binary search」看 距離<=X 有幾組
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # binary search 重點有2個：判斷的函式、while left<right 猜數字
        def findPairs(X):  # binary search 判斷的函式，找 nums 中「距離<=X」有幾組
            ans = 0  # 利用「毛毛蟲」爬行，累積找到「有幾組答案」
            j = 0  # 尾j
            for i in range(len(nums)):  # 頭i 往右跑
                while nums[i]-nums[j]>X:  # 數字差太多時
                    j += 1  # 尾巴往右縮
                # 離開迴圈，表示這是「頭在i」時，頭尾長度的範圍
                ans += i-j  # 所以「頭在i」時，有i-j組 的距離在範圍內（合理）
            return ans  # 「距離X」時，總共合理的組數

        nums.sort()  # 先從小到大排好，以便用「毛毛蟲」的方法，找有幾組答案
        left, right = 0, nums[-1]-nums[0]  # 猜數字的左界、右界（猜距離值
        while left<right:  # binary search 作法：只要（範圍太大）就繼續猜
            # print(left, right) 我常印出 左界、右界，來debug，看哪裡寫錯
            mid = (left+right) // 2  # 猜（左右界）中間的數字
            if findPairs(mid)>=k:  # 猜的答案，對應的 pairs數，若超過題目要求的k
                right = mid  # 就更新右界
            else:  # 不夠的話，要更新左界
                left = mid + 1  # mid 不夠，所以合理的左界範圍，要+1
        return left  # 最後離開迴圈時，left和right會夾擊出答案（猜中答案）
