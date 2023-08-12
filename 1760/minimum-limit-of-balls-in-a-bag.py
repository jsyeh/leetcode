# 希望 bag 裡的球越少越好。所以你可挑任一bag把它分兩袋。
# 暴力法應該是「挑最大袋」把它均分。但是 10^9 沒辦法做這麼多次
# binary search 能怎麼用呢？ 就直接預測最大值！然後看「能不能做到」
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()
        N = len(nums)
        def possible(bagV: int) -> bool:
            # 先 binary search 找到關鍵的位置
            # 再逐一查「會用到幾個k值」
            left, right = 0, N
            while left<right:
                mid = (left+right) // 2
                if nums[mid]==bagV:
                    break;
                if nums[mid]<bagV:
                    left = mid+1
                else:
                    right = mid
            # 現在 left 會是開始點
            op = 0
            for i in range(left, N):
                now = nums[i]//bagV 
                if nums[i]%bagV > 0: now += 1
                op += (now-1)
                if op>maxOperations: return False
            return True # bag容量V是否可行？
        
        # F F F ... F T T ... 找到第1個 T 的意思，因為它會最小
        # 所以問題就反過來問：不可能的最大值
        left, right = 1, nums[N-1]
        while left < right:  # 希望 left是F, right是T
            mid = (left+right) // 2
            # print(left, mid, right)

            if(not possible(mid)): left = mid + 1 # 不可能，就放寬條件
            else: right = mid # 可能嘛，再繼續挑戰
        
        # return left + 1 # 因為 left 是不可能的最大值，答案要再大1格?
        return left
# case 52/58: [1] 1
