# LeetCode 648. Replace Words
# 英文字有「字根root」，代表字的意思。
# 在 dictionary 有許多「字根root」，
# 用它取代某些字首相同的字。
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = set(dictionary) # 把字典裡的字根root加入 d 裡面，方便快速查找
        ans = []  # 用來放答案的字
        s = sentence.split()  # 把「句子」斷字
        for word in s:  # 把句子裡，每個字逐一查「有沒有字根符合」
            found = False
            for i in range(1,len(word)):  # 從短到長，去查字根
                if word[:i] in d:  # 這個長度的字，有在字典出現過
                    ans.append(word[:i])  # 馬上加入答案
                    found = True  # 標註「找到了」
                    break
            if not found:  # 若都「沒找到答案」
                ans.append(word)  # 那整個字都加入答案
        return ' '.join(ans)
