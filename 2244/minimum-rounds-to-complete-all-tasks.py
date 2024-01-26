# 每次能解決 2 or 3 個「等級相同」的 task
# 問要做幾次。可使用 Counter() 來決定工作
# 
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks) # 統計「同等級」各有幾個
        ans = 0 # 要幾個 round 才做得完
        for c in counter:
            if counter[c]==1: # 若只有1個
                return -1 # 就無解
            if counter[c]%3==0:
                ans += counter[c]//3
            else: # 餘1 or 餘2 都可多做1次解決
                ans += counter[c]//3 + 1
        return ans
