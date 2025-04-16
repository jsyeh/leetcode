# LeetCode 2537. Count the Number of Good Subarrays
# nums 有幾種 subarray，裡有 k 組以上 arr[i]==arr[j]，可用 sliding window 「毛毛蟲」解法
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        counter = Counter()  # 快速統計「有多少重覆的數字」
        ans = pairs = 0  # 答案一開始是0， pairs 組數也是 0
        head = tail = 0  # 毛毛蟲，左邊尾巴、右邊頭
        while head < N:  # 以 head 為主，左邊 tail 「拖多長」就加答案
            now = nums[head]  # 右邊頭「吃下數字
            pairs += counter[now]  # 對應「增加的 pairs 數」
            counter[now] += 1  # 對應數量增加
            head += 1  # 吃完後，頭往右移，等下一輪再吃
            while pairs >=k:  # 開始縮「左邊的尾巴」
                now = nums[tail]  # 尾巴吐出來
                counter[now] -= 1  # 對應數量變少
                pairs -= counter[now]  # 對應「減少的 pairs 數」
                tail += 1  # 吐完後，尾巴往右移
            # 到這裡的話，就是tail比「足夠」再少1，對應答案總數，會有tail組
            ans += tail
        return ans
