# 先 parse expression 以 operator 來斷開
# table[left][right] 表示 數字 left ... right 的答案有哪些 List[int]
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []

        # parse expression
        nums, op = [], []
        now, N = 0, 0
        for c in expression:
            if c >= '0' and c <= '9': # 數字
                now = now * 10 + int(c)
            elif c=="+" or c=="-" or c=="*":
                nums.append(now) # 現在是某筆資料，加入
                op.append(c)
                now = 0 # 之後是新的數字，所以這裡清為0
                N += 1 # 這會決定陣列的大小，方便後面迴圈處理
        nums.append(now) # 最後一筆資料，也需要加入
        # print(nums)
        # print(op, N)

        # table[i][j] 表示 nums[i]...nums[j] 的答案，會是 List
        table = [[None]*(N+1) for _ in range(N+1)] 
        for i in range(N+1):
            table[i][i] = [nums[i]] # 裡面放 List
        # print(table)

        def helper(left: int, right: int)->List[int]:
            # print(left, right)
            if table[left][right] != None: # 如果之前有備份過
                return table[left][right] # 就直接拿備份的答案來用

            ans = [] # 先是空集合，等下會一直append()
            for k in range(left, right):
                part1 = helper(left, k)
                part2 = helper(k+1, right)
                for a in part1:
                    for b in part2:
                        if op[k]=="+": ans.append(a+b)
                        if op[k]=="-": ans.append(a-b)
                        if op[k]=="*": ans.append(a*b)
            table[left][right] = ans # 備份答案，以便之後可加速
            return ans

        return helper(0,N) # nums[0]...nums[N] 及 N 個op
