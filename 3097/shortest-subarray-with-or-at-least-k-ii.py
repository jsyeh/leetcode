# LeetCode 3097. Shortest Subarray With OR at Least K II
# 一堆數字「越 OR 越大」，因有「越來越多的1」。目標：用「連續的最少的數字」， OR 的結果，最少要是 k
# 數字太多了，可用「毛毛蟲」式的sliding window 來解，用 O(n) 完成
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def findBits(bits):  # 從「累積的bits[i]裡，找出全部OR的結果
            ans = 0
            for i in range(32):
                if bits[i]>0: ans += (1<<i)
            return ans
        def incBits(bits, now):  # 把 now 的 bits 都加到 bits[i]
            for i in range(32):
                if (now & (1<<i))>0: bits[i] += 1
        def decBits(bits, now):  # 
            for i in range(32):  # 把 now 的 bits 都減掉 bits[i]
                if (now & (1<<i))>0: bits[i] -= 1
        # 為了讓「下面」程式碼簡單，「上面」建了3個函式
        bits = [0] * 32  # 共有 32 個 bit，把每個bit看「累積」幾個「重覆的1」
        ans = inf  # 因要找「最小值」，預設值就先設「無限大」
        left = 0
        for right in range(len(nums)):  # 毛毛蟲的右邊
            incBits(bits, nums[right])  # 把 nums[right] 的 bits 加入 bits[i]
            while findBits(bits)>=k and left<=right:  # OR 的結果，最少要是 k。合理，就「左邊縮短」
                ans = min(ans, right-left+1)  # 縮短前，先「更新答案」
                decBits(bits, nums[left])  # 左邊縮短
                left += 1  # 左邊縮短
        if ans==inf: return -1  # 若是預設值「無限大」表示「沒找到答案」，回傳 -1
        return ans
