# 策略：(1)不符合題目要求的作法，直接for迴圈找答案
# (2) 先利用 binary search 找到rotated 的交界點，再用 binary search 找值
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ans = -1
        # for i in range(len(nums)):
        #     if nums[i] == target: return i
        # return ans
        # 題目要求的 O(logN)，上面是 O(N) 不符合
        # 下面改用 binary search 法 2次，希望符合 O(logN)
        N = len(nums)
        if N == 1 and nums[0] == target: return 0
        if N == 1 and nums[0] != target: return -1

        left, right = 1, N # 要看誰比nums[0]小
        while left < right:
            mid = int((left+right)/2)
            if nums[0] < nums[mid]: # 0...mid還算正常，問題在右邊
                left = mid+1
            else: right = mid
        pivot = left
        # print(pivot)

        left, right = 0, N # 還是照舊的 binary search寫法
        while left < right:
            mid = int((left+right)/2)
            mid2 = (mid+pivot)%N # 只是多計算 mid2 以便轉到 rotated 世界的坐標
            # print(left, right, mid, mid2)

            if nums[mid2] == target: return mid2
            if nums[mid2] < target: left = mid + 1
            else: right = mid
        # 離開迴圈有兩種可能：找不到 or 剛好找到了
        left2 = (left+pivot)%N
        if nums[left2] == target: return left2
        else: return -1

