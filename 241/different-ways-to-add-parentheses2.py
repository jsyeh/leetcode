# LeetCode 241. Different Ways to Add Parentheses
# 加「圓括號」可任意調整「運算符號」的優先順序，找出「全部可能的值」
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 先拆解 expression，分別斷字成 nums[i] 及 op[i]
        now = 0 # 用來「結合成現在的數字」
        op, nums = [], []
        for c in expression:
            if c.isdigit(): now = now * 10 + int(c) # 數字「慢慢成形」
            else: # 若遇到「運算符號」
                op.append(c) # 就記下 op[i]
                nums.append(now) # 就塞入 nums[i]
                now = 0 # 數字再清空，等下一筆「慢慢成形」
        nums.append(now) # 塞入最後1個數字，現在 N 個 nums 對應 N-1 個 op
        N = len(nums)
        @cache
        def helper(left, right): # 利用「函式呼叫函式」來解
            if left==right: return [nums[left]]
            ans = []
            for k in range(left, right): # 挑第k個數/第k個op
                part1 = helper(left, k) # 左邊一堆
                part2 = helper(k+1, right) # 右邊一堆
                for p1 in part1: # 排列組合：左邊挑1個
                    for p2 in part2: # 右邊挑1個，進行配對，算出可能的1個答案
                        if op[k]=='+': ans.append(p1+p2)
                        elif op[k]=='-': ans.append(p1-p2)
                        else: ans.append(p1*p2) # 將答案塞入 ans 裡
            return ans # ans 裡有滿滿的答案
        return helper(0,N-1) # N 個數，對應 nums[0]...nums[N-1]
