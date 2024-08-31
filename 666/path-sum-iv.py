# LeetCode 666. Path Sum IV
# 題目將 tree 的nodes變成一堆「3位數」：depth(1-4),position(1-8),value(0-9)
# 想到可照「資料結構」課本介紹過的，「用另一個array」來表示tree裡的值。
# tree[0] 再 tree[1] tree[2] 再 tree[3]...tree[6] 再 tree[7]...tree[14]
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = [[0],[0,0],[0,0,0,0],[0,0,0,0,0,0,0,0]]  # 每層各有 1 + 2 + 4 + 8
        non_leaf = [[0],[0,0],[0,0,0,0],[0,0,0,0,0,0,0,0]]  # 每層各有 1 + 2 + 4 + 8
        for num in nums: # 先建好 tree[d][p]
            d, p, v = num//100-1, num//10%10-1, num%10  # 百位、十位、個位
            # d 和 p 都 -1 是想變成 0-index
            tree[d][p] = v  # 將 tree 的座標，換算成 array index
            if d>0: non_leaf[d-1][p//2] = 1 # tree[d][p]樓上的node就「不是葉子」哦！
        ans = 0
        for num in nums: # 再重走一次 tree
            d, p, v = num//100-1, num//10%10-1, num%10  # 百位、十位、個位
            # d 和 p 都 -1 是想變成 0-index
            if non_leaf[d][p]: continue # 「不是葉子」，就避開
            while d>=0:
                ans += tree[d][p]
                # print(tree[d][p], end=' ')
                d -= 1
                p //= 2
        return ans

