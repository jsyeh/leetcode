# words 裡有很多個「英文字」，chars 裡面有很多個「字母」
# 如果英文字「能被」chars字母組出來，長度便增力。想知能增加的總長度
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        d = defaultdict(int) # 先統計 chars 裡字母各有幾個
        for c in chars: 
            d[c] += 1 # 先統計 chars 裡有字母有幾個

        for word in words:
            d2 = defaultdict(int) # 再統計「字」裡字母各有幾個
            for c in word:
                d2[c] += 1 # 統計「字」裡字母各有幾個

            # 再逐一比對，看 d 的字「夠不夠用
            bad = False # 一開始還沒有壞
            for c in d2: # c是字母，n是對應的字
                if d[c]<d2[c]: # 字母不夠用
                    bad = True
                    break
            if not bad: # 如果沒有壞掉
                ans += len(word) # 答案就增加
        return ans
