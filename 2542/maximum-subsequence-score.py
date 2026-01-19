# LeetCode 2542. Maximum Subsequence Score
# 挑 k 個 index, 讓 nums1 對應的 k 個數加加，再乘 min(nums2對應k個數) 希望最大
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        a = [ (nums2[i],nums1[i]) for i in range(len(nums1))]
        a.sort(reverse=True)  # 以 nums2[i] 為主，大到小排序
        heap = []
        sum1 = 0  # 目前範圍的 nums1 加總
        for i in range(k):  # 前 k 項「大的nums2」放入 heap
            heappush(heap, a[i][1] )  # 塞入 num1（對應「大的nums2」 ）
            sum1 += a[i][1]  # 加入 num1
        
        ans = sum1 * a[k-1][0]  # a[k-1][0] 是 min(nums2[:k])

        for i in range(k,len(nums1)):  # 後面繼續更新
            heappush(heap, a[i][1] )  # 依序塞入「大的nums2」對應的 num1
            num1 = heappop(heap)  # 吐掉小的數
            sum1 += a[i][1]  # 新加入、對應第i大的 a[i] 的 num1
            sum1 -= num1  # 出最小的 num1
            ans = max(ans, sum1 * a[i][0])  # 更新答案，找最大的 sum1 * min(num2)
        return ans
