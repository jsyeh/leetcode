# 原本想用 hashset 找「重覆出現的字」不過，題目限定「constant extra space」
# (1) 不能開太多。突然有了靈感，就是 XOR 出來的結果。
# 因為題目說 1...n 的數，多出來1個數，就xor就出來了。但可能重覆很多次，糟！
# (2) 也不能暴力去試，因 10^5 * 10^5 就超時
# (3) 也不能做 sort 因題目說不能動到 nums[i]陣列
# (4) 看了 Editorial 裡，介紹好多「不合乎題目要求」的作法，增廣見聞，好帥
# (5) 最後看到 binary search 法，去巡「哪個數字」以下出現的次數超過範圍，讚！
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)  # 因為 nums[i] 裡多一個數，上限應是N-1
        def upperBound(bound) -> bool:
            count = 0
            for num in nums: # 有幾個比 bound 小的數
                if num<=bound: count += 1
            if count>bound: return True # 數字暴棚，便是合理的上界
            else: return False # duplicate 不在這個 bound 裡
        
        left, right = 1, N
        while left<right:
            mid = (left+right) // 2
            if upperBound(mid): # mid 是合理的上界
                right = mid
            else:
                left = mid + 1 # 大概了解 binary search 的 +1 寫法了
        return left # 每次先用 left 看對不對，再梢微調整即可

'''
        # 稍早想到的 XOR 的方法不行，因可能重覆很多次、有些數字不出現
        XOR0 = 0 # 原本 1...N 合起來
        XOR1 = 0 # 原本 1...N 合起來，再加上1個介於1...N的數
        for i in range(1,N): XOR0 ^= i
        for i in range(N): XOR1 ^= nums[i]

        return XOR0 ^ XOR1
'''
# case 18/58: [2,2,2,2,2] 天啊，竟然重覆這麼麼多次！我的演算法完全錯誤
# "...which appears two or more times."
