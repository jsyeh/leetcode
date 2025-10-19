# LeetCode 1625. Lexicographically Smallest String After Applying Operations
# 字串（偶數長度）裡面像數字一樣，可以 (1) 將 a 加入每一個「奇數位數」，超過就 % 10
# (2) rotate b位，其中 rotate right 像 3456 變成 6345 把6移到最左邊，其餘往右移1格。
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # 其實，把所有的可能都查過一次，即可知道答案
        ans = s  # 都不套用任何操作，先當作答案。之後再更新成「更小」的字串
        N = len(s)
        s = list(s+s)  # 把字串變整數陣列，方便修改；2倍方便 rotate
        for t1 in range(10):  # 操作(1) 將「奇數位數」加 a % 10，最多做10次（會循環）
            for k in range(1, N*2, 2):  # 奇數位數，但若b是奇數，便能將所有可能都變動
                s[k] = str((int(s[k]) + a) % 10)  # 先變整數、再加、取餘、再變回字串
            for rot in range(N):  # 操作(2) rotate right 最多做 N 次（會循環）
                start = (rot*b) % N
                ans = min(ans, ''.join(s[start:start+N]))
                if b%2==1:  # 如果 rotate 的量是奇數，便有可能「將全部的位數」都輪過一次
                    for t2 in range(10):  # 操作(1) 便能「也」對「偶數位數」發生效果
                        for k2 in range(0, N*2, 2):  # 對「偶數位數」做修改
                            s[k2] = str((int(s[k2]) + a) % 10)
                        ans = min(ans, ''.join(s[start:start+N]))
        return ans
