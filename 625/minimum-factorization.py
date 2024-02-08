# 找到最小的 x ，它的每一位數，乘起來後，是 num。
# 想要最小，所以 (1) 相乘的數字要少，(2) 小的數字先放
# ex. 48 可分成 6x8 也可以分成 2x4x6 要用少的數
class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num==1: return 1 # 特殊狀況：1 （因為後面只處理2到9）
        ans = []
        for d in range(9,1,-1): # 由大到小9...2，測每一位數，並記下來
            while num%d==0: # 可以整除
                ans.append(str(d)) # 答案(以字母)「大到小」串起來
                num //= d # 目標的數字就變小了
        if num!=1: return 0 # 若數字除不盡 ex. 11
        
        ans = int(''.join(ans[::-1])) # 把ans[::-1]字母倒過來，再join串起來
        if ans>=2**31: return 0 # 若數字>32-bit能顯示的範圍
        return ans
        # 最後一行的意思，是先 
# 題目的例外狀況：如果找不到答案（即最後 num 沒辦法除到給成1 或數字放不進32-bit
# case: 1 # 
# case 12/146: 11
