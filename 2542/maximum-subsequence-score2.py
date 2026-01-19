# LeetCode 2542. Maximum Subsequence Score
# 挑 k 個 index, 讓 nums1 對應的 k 個數相加，再乘 min(nums2對應k個數) 希望最大
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        a = [(n2,n1) for n1,n2 in zip(nums1,nums2)]
        a.sort(reverse=True)  # 先湊 k 組數，把前k大的nums2取出
        heap = [a[i][1] for i in range(k)]
        heapify(heap)  # 之後將小到大依序吐掉 nums1 的這k個數，換加入新的n1,n2組
        total = sum(heap)
        ans = total * a[k-1][0]  # 前k項的nums1 及對應最小的 nums2 相乘

        for i in range(k,len(nums2)):  # 後面將加入的數
            n2, n1 = a[i]  # 將加入的對應的數
            heappush(heap, n1)  # 加1
            total += n1 - heappop(heap)  # 加1、吐1
            ans = max(ans, total*n2)  # 更新答案
        return ans
