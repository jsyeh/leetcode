# 想算出2個數列的 abs sum diff 也就是 sum |相減|
# 可把 nums1 裡其中一個數，換成另一個（也在nums1裡的）數
# 數字超多 10^5，暴力試（挑10^5某數放10^5某格），會超時
# 參考 vortrubac 的解題策略，看nums1裡，誰最近。所以 sorted拿來用
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        sorted1 = nums1.copy()
        sorted1.sort()
        print(sorted1)

        better = 0 # 修改後，有變更好嗎？ (abs(diff)變更小)
        for i in range(N):
            a, b = nums1[i], nums2[i]
            oldDiff = abs(a-b)
            # 接下來 binary search 在 sorted1[] 裡找 最接近 b 的數
            left, right = 0, N
            while left<right:
                mid = (left+right)//2
                if sorted1[mid]<b: # 要再右邊一些
                    left = mid + 1
                else:
                    right = mid
            # if left!=N: print(a, b, sorted1[left])
            # else: print(a, b, "biggest") # 測試發現在 left-1..left 間
            if left==N: # 最右邊的話，要測 sorted[N-1]
                nowDiff = abs(sorted1[N-1]-b)
            elif left==0: # 最左邊的話，要測 sorted[0]
                nowDiff = abs(sorted1[0]-b)
            else: # 其他，要測 sorted[left-1] 及 sorted[left]
                nowDiff = min(abs(sorted1[left-1]-b), abs(sorted1[left]-b))

            if oldDiff-nowDiff > better:
                better = oldDiff - nowDiff # 變更好的量
            
        ans = - better
        for i in range(N):
            ans += abs(nums1[i] - nums2[i])
            ans %= 1000000007
        return ans
        # 全部加起來的 sum|diff| - better 
