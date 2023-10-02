class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        table = {}
        for c in s: # 逐個字母統計
            if c not in table:
                table[c] = 1
            else:
                table[c] += 1
        # 要確認全部的 frequence 是否相同
        freq = -1
        for c in table:
            if freq==-1: # 第一個 frequence 記入 freq
                freq = table[c]
            else: # 後續全部的字母
                if table[c]!=freq: # 只要與 freq 不同
                    return False # 就是失敗
        return True # 全部檢測都合格, True

        
