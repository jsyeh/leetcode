# 這題比較特別, 是規定你只能用 mountain_arr.get() 和 mountain_arr.length(), 去找出 target
# 而特別的是, array 裡分成 左邊增加、右邊減少, 有個最高的值 peak 但你不知道它在哪裡。
# 所以 (1) 先把 peak 找出來, (2) 左邊找 target, (3) 右邊找 target
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()

        # (1) 先把 peak 找出來
        left, right = 0, N-1 # 基本上 binary search 會用 N, 但因找 peak 要2格,所以再-1
        while left<right:
            mid = (left+right)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1): # 左半邊順向, 答案在右半
                left = mid + 1
            else:
                right = mid
        peak = left # 找到 peak 了
        # print(peak, mountain_arr.get(peak))

        # (2) 左邊找 target
        left, right = 0, peak+1 # 右不包含
        while left<right:
            mid = (left+right)//2
            now = mountain_arr.get(mid)
            if now == target: return mid
            if now<target:
                left = mid + 1
            else:
                right = mid
        
        # (3) 右邊找 target
        left, right = peak, N # 右不包含
        while left<right:
            print(left, right)
            mid = (left+right)//2
            now = mountain_arr.get(mid)
            if now == target: return mid
            if now<target: # 要記得倒過來哦
                right = mid # 要記得倒過來哦
            else:  # 要記得倒過來哦
                left = mid + 1 # 要記得倒過來哦

        return -1
# case 77/79: [0,5,3,1]
