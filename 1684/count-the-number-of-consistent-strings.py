# 如果 words 裡的 word 只有 allowed 的字母，很好！
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed) # 轉成 set()
        ans = 0
        for word in words:
            bad = False # 一開始沒有壞
            for c in word: # 逐個字母檢查
                if c not in allowed: # 用到不允許的字母
                    bad = True # 就壞掉
                    break
            if not bad: # 若沒壞掉
                ans += 1
        return ans
