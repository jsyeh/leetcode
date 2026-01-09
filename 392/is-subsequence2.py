# LeetCode 392. Is Subsequence
# 找一下 s 是否為 t 的 subsequence，也就是「照順序出現」（可跳過一些）
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0: return True  # 不用比啦，直接就成功！
        # 用迴圈，照著找 s 的每個字母。找到再接著找「下一個字母」
        i = 0  # 想逐一找 s[i] 的字母
        for c in t:  # 備選的 t 字串，把字母「一個個拿出來比對」
            if s[i] == c: i += 1  # 順利找到 s[i] 字母，換下一個 s[i]
            if i >= len(s): return True  # 湊齊 s 的全部字母，成功
        return False  # 沒有成功，就失敗
