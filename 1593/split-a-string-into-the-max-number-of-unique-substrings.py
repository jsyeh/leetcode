# LeetCode 1593. Split a String Into the Max Number of Unique Substrings
# 將 s 分成很多「不相同」的小字串，儘量切碎、最多小段的小字串。最多有 16 個字母，用 backtrack 暴力試
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)
        used = set()  # 利用 set() 可快速找到「使用過的字串」
        # ansStr = []  # 供 Debug 時，研究目前對應的 ans 字串
        self.ans = 0  # 最後放答案的地方。不加 self 會出錯，只好用 self.ans
        def helper(i):
            if i==N:
                # print(ansStr)  # 供 Debug 時，研究目前對應的 ans 字串
                self.ans = max(self.ans, len(used))
            for j in range(i+1,N+1):
                if s[i:j] not in used:  # 利用 set() 可快速找到「使用過的字串」
                    # ansStr.append(s[i:j])  # 供 Debug 時，研究目前對應的 ans 字串
                    used.add(s[i:j])  # 暫時使用 s[i:j] 這個字
                    helper(j)  # 函式呼叫函式「再深入試」
                    used.remove(s[i:j])  # 再放棄這個字
                    # ansStr.pop()  # 供 Debug 時，研究目前對應的 ans 字串
        helper(0)  # 從頭開始，試著斷字看看
        return self.ans

