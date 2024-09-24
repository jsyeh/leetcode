# LeetCode 491. Non-decreasing Subsequences
# 找出一堆 subsequences 裡面數字是「慢慢增加」（可相同）
# 因為 input 數字很少 15 個數，可以暴力試出來。
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()  # 擔心有重覆的答案，所以用set收集
        now = []  # 現在收集到的「慢慢增加」的數列
        N = len(nums)
        def helper(i):
            print(now)
            if i==N:  # 終止條件：做最後做處理
                if len(now)>=2:  # 合理的長度
                    ans.add(tuple(now))  # 把數列轉成 tuple 才能放入 set
                return  # 停止繼續計算

            # 可使用這個數，也可不要用這個數
            if len(now)==0 or nums[i] >= now[-1]: # 合規定
                now.append(nums[i])  # 先用這個數
                helper(i+1)  # 再往下問
                now.pop()  # 避開這個數
            helper(i+1) # 再往下問
        helper(0)
        return ans
        
