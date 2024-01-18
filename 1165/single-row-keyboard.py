# 超長的 keyboard 有字母，你要打 word 裡的字
# 如果你只用1個手指打字，一開始在位置0， 手指總共要移動多遠？
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # 先建立 keyboard 的 key 對照表
        pos = {} # 用字典來存位置
        for i in range(26):
            pos[keyboard[i]] = i # 記下對應的位置
        ans = 0 # 總共要移動的距離
        finger = 0 # 一開始「手指」的位置
        for c in word: # 接下來「逐字」計算距離
            ans += abs(pos[c]-finger) # 增加移動的距離
            finger = pos[c] # 記錄現在的位置
        return ans
