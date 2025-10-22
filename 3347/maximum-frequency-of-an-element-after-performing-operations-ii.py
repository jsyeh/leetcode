# LeetCode 3347. Maximum Frequency of an Element After Performing Operations II
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        N = len(nums)  # 陣列的長度
        nums.sort()  # 先把數字排序
        counter = Counter(nums)  # 累計「每個數」出現次數
        # 第一次「毛毛蟲」技巧，用「毛毛蟲」的觀念，找出「上下各差k的狀況」
        ans = low = high = 0  # low在左邊、high在右邊
        for mid in range(N):  # mid在中間，逐漸往右移
            while nums[mid]-nums[low] > k:  # 下界 low 超過範圍
                low += 1  # 下界 low 往 mid 移
            while high+1 < N and nums[high+1]-nums[mid] <= k:  # high 可擴展
                high += 1  # 上界 high 往外移
            # 可到這裡，代表 low-mid-high 的範圍內的數(共high-low+1)，都可集中在 mid
            now = min(counter[nums[mid]] + numOperations, high-low+1)  # 有「次數限制」
            ans = max(ans, now)  # 有種例外，是「缺少中間的數」，要用第二次 「毛毛蟲」技巧
        left = 0  # 第二次「毛毛蟲」技巧，找到左右「最長的範圍」裡面的數差 2k
        for right in range(N):  # 「右界」逐一右移，以「右界」為主 2k的範圍，若「左界」超過範圍
            while nums[right]-nums[left] > 2*k: left += 1  # 「左界」快跟上
            now = min(numOperations, right - left + 1)  # 不是「無限多次」有「次數限制」
            ans = max(ans, now)
        return ans
