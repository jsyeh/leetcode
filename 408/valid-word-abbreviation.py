# 有些「縮寫」的規則：數字展開、補空格的地方
# 但有些是錯的：連續2個數字、數字0開頭、數字是0
# 判斷是否能展開，且「不是錯的」。
# 在submit前，要將「For example」裡全部試過一次，確認沒有漏規則。
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        N = len(word)
        i = 0 # 對應 word[i]
        shift = 0 # 對應「要跳掉」的格子數
        numbering = False
        for c in abbr:
            if c.isdigit():
                if shift==0 and int(c)==0: # leading zero
                    return False # 違反規則2
                shift = shift * 10 + int(c)
                numbering = True # 開始有數字
            else: # 不是數字，是字母，就往右移
                if numbering and shift==0: # replaces an empty substring
                    return False # 違反規則3
                numbering = False # 切回「不是數字」
                i += shift # 但要檢查字是否超過範圍
                shift = 0
                if i<N and c==word[i]: # 很好
                    i += 1 # 比對成功
                else: # 比對失敗
                    return False
        if i+shift!=N: return False# 最後收尾時，要看是否長度一致
        return True
