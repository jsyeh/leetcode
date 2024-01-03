# 鍵盤有些 brokenLetters 打不出某些字。請問 text 裡, 有幾個字是打得出來的
# 所以要先把 text 斷字, 再逐字檢查, 看能完成幾個字
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        badKeys = set(brokenLetters) # 先把壞掉的字, 給成 hashset 方便快速查找
        ans = 0
        for word in text.split(): # 把 text 斷字後, 一次取一個 word 處理
            bad = False # 一開始沒有壞掉
            for c in word: # word裡的母個字母 c
                if c in badKeys: # 如果 c 是壞掉的鍵
                    bad = True # 就壞掉了
                    break # 且提早離開、不用再測其他字母
            if not bad: ans += 1 # 這一輪 word 若都沒有壞掉, 便找到1個好的 word
        return ans
        
