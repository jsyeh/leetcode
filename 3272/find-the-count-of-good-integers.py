# LeetCode 3272. Find the Count of Good Integers
# n位數中（最多10位數），有幾個數「可重新排列」後，「成為 k 倍數的迴文」
# ex. 2020 可排成 2002 且是 k=2 的倍數（k是 1...9）
class Solution:  # 我有參考 lee215 的解法
    def countGoodIntegers(self, n: int, k: int) -> int:
        visited = set()  # 試過的，不要再重覆算
        n2 = (n+1) // 2  # 先試一半位數，8位數就試4位，7位數也試4位
        ans = 0  # 迴文：先試一半、再鏡射出全部，檢查是否是 k 的倍數。再依字母「排列組合」
        for v in range(10**(n2-1), 10**n2):  # ex. 1000 試到 9999
            now = str(v) + str(v)[::-1]  # 從「一半」鏡射出「全部」
            if n%2==1: now = str(v) + str(v)[::-1][1:]  # 奇數長度的鏡射，要少1個字母
            key = ''.join(sorted(list(now)))  # 「小到大排好」字串當 key
            if int(now) % k == 0:  # 符合題目要求「k的倍數」
                if key not in visited:  # 若此 key 沒出現過，就可「排列組合」
                    visited.add(key)  # 加入 visited 用過以後不要再用
                    counter = Counter(now)  # 依照「統計結果」排列組合
                    # n 位數，排列組合是 n! 階乘，但如果重覆的階乘要在分母除掉
                    if counter['0']==0: p = factorial(n)  # n! 階乘，Python 用 factorial(n)
                    else: p = (n-counter['0']) * factorial(n-1)  # 若有'0', 開頭要先避開 0
                    for v in counter.values():  # 針對每種字母，看它的重覆狀況
                        p //= factorial(v)  # 分母除掉「很多個小的階乘」、除掉「重覆的各種」
                    ans += p  # 最後，更新答案
        return ans
