# LeetCode 3042. Count Prefix and Suffix Pairs I
# 左邊 words[i] 是不是 右邊 words[j] 的prefix兼postfix (剛好是字首、也是字尾)
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        N = len(words)
        for i in range(N):  # 左邊 words[i] 
            L = len(words[i])
            for j in range(i+1, N):  # 是不是右邊 words[j] 的字首兼字尾
                if words[i] == words[j][:L] and words[i] == words[j][-L:]:
                    ans += 1
        return ans
