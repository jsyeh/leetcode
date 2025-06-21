# LeetCode 3085. Minimum Deletions to Make String K-Special
# word 要刪掉幾個字母，能讓 abs( freq(word[i]) - freq(word[j]) ) <= k
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        ans = inf
        for c in counter:  # 先挑1個數不動，當成「最小的數」
            now = 0
            for c2 in counter:  # 其他人都要配合它，看有無機會做到
                if counter[c2] > counter[c] + k:  # 多很多
                    now += counter[c2] - counter[c] - k  # 裁多的部分
                elif counter[c2]<counter[c]:  # 更少，不行！
                    now += counter[c2]  # c2字母全刪掉
            ans = min(ans, now)
        return ans
        # 註：本來以為「只要以最小值 m 為準」，所有人都要 <= (m+k)
        # 但沒想到「把最小的值刪掉」也可以成功！
