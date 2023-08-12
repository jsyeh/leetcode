# 三角形3個邊：兩邊相加>長邊，所以這題要先將邊排序
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        print(nums)

        ans = 0
        for i in range(N-2): # 第1個最短邊
            for j in range(i+1, N-1): # 第2個邊
                # print("i/j: ", i, j)
                # print("val: ", nums[i], nums[j])

                sum = nums[i] + nums[j]
                # 再用 binary search 找第3個邊的最小值，右邊就全是答案
                left, right = j+1, N # 右不包含
                while left+1<right:
                    mid = (left+right) // 2
                    # print(left, mid, right)
                    if sum>nums[mid]: # 合理的第3邊，太好了
                        left = mid # 還可以再多逼近一些
                    else: # 太長了/不行，無法組三角形
                        right = mid
                # print("left:", left, " left-j:", left-j)
                # 離開迴圈時，left是第3邊
                if sum>nums[left]:
                    ans += left - j # 
                    # print("=====got it")

        return ans
