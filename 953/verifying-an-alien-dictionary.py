# 外星人用的奇怪字典，對應的a...z是不同的，要翻譯一下
# 如果 words 裡的word是照「外星人」的字母排序好，就True
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien = defaultdict(int)
        for i,c in enumerate(order): # 照著 order 建對照表
            alien[c] = i # 外星人的字母對照表，對應外星人的「字母序」
        for i in range(len(words)-1): # words[i] vs. words[i+1]
            for k,c in enumerate(words[i]):
                if k<len(words[i+1]): # 在長度範圍內
                    print(c, words[i+1][k])
                    if alien[c] > alien[words[i+1][k]]:
                        return False # 順序不合理，失敗
                    elif alien[c] < alien[words[i+1][k]]:
                        break # 合理，離開此迴圈，下一筆
                else: # 長度不合理，words[i]太長
                    return False # 前面都相同，但words[i]太長，也失敗
        return True # 檢測合格
