# 之前寫過兩種寫法：利用used 避開挑過的數 or 挑某數，排列組合子問題，再逐一再補到前面
# 這些寫法，都有用到「函式呼叫函式」的技巧。
# 這次用for迴圈挑「沒挑過」的數，配合 used[i] 避開挑過的數，再還原
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        used = [False]*N # 一開始數字都沒被挑過
        # 定義函式，暴力挑數字
        def bruteforce(remains) -> List[List[int]]: # 回傳(子問題)全部的組合
            if remains==0: # remains 剩下能用的數，用來當終止條件
                return [[]] # 剩0個數，就是1個空集合。還是能讓呼叫著能湊出需要的組合
            ans = [] # 如果有剩數字能用，就開始收集答案
            for i in range(N): # 迴圈挑選「這一」bruteforce()要挑的數
                if used[i]==False:
                    used[i] = True # 決定挑選 nums[i]
                    subLists = bruteforce(remains-1) # 函式呼叫函式的子問題
                    for subList in subLists: # 子問題的答案
                        subList.insert(0, nums[i]) # 前面補上 nums[i] 便是...
                        ans.append(subList) # 便是現成的一組答案
                    used[i] = False # 還原 num[i]
            return ans

        return bruteforce(N)
