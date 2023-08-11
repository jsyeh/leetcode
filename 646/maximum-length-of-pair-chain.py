# 想讓 Pair 可以 chain 起來，所以可以讓 HashMap 對照。
# 先照前面的數排序，再照著Pair查看看可以對照 Pair長度
# 和 368. Largest Divisible Subset 有點像，就做個 HashTable 吧

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        N = len(pairs)
        pairs.sort(key=lambda x:x[1]) # 以結尾做排序
        # 以便「往前」查看「能接到誰」
        # print(pairs)

        ans = 1
        length = {}
        for i in range(N):
            length[i] = 1
            # 糟，我不會用 bisect_left() 還是用暴力的笨方法吧
            for k in range(i, -1, -1):
                if pairs[k][1] < pairs[i][0] and length[k]+1>length[i]:
                    length[i] = length[k] + 1
                    if length[i] > ans: ans = length[i]
                    
        return ans

