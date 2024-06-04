# 用字串來表示數字，數字超長的，有10^5 位數。
# 那麼能用這個字串，做出的「最大的迴文」是多大呢？
# 使用 greedy 演算法，靠直覺，先把大的數放在外面
# 再慢慢放小的數在裡面即可。
# 但如果只有1個數的話，就只能放中間了
class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = Counter(num)
        prefix = []
        odd = []
        for i in range(9,-1,-1):
            k = counter[str(i)] // 2
            # 特別處理'0'不能在兩端，除非有人先卡在前面
            if i!=0 or (i==0 and len(prefix)>0):
                for _ in range(k):
                    prefix.append(str(i))
            if counter[str(i)]%2==1:
                odd.append(str(i))  # 其實只取最大的 odd[0]
        postfix = list(reversed(prefix))
        if len(prefix)==0 and len(odd)==0: # 什麼都沒有, 可能是1萬個0
            return '0'
        if len(odd)>0:
            ans = prefix + [odd[0]] + postfix
        else:
            ans = prefix + postfix
        return ''.join(ans)
# case 66/67: 有 1萬個0
