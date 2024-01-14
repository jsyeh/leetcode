# 這題與 758. Bold Words in String 一樣。我之前算得太慢，這裡重寫
# 不自己裁字母，而是以 word 為主，.find(word)逐格去找，或許更快
# 有點仿 Editorial 的思緒
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        N = len(s)
        bold = [False]*N # 用來標示是否為「粗體字」
        for word in words: # 以 word 為主，逐格去找
            lenW = len(word) # 想省一點時間
            now = s.find(word) # 第一次找word
            while now != -1: # 有找到
                for k in range(now, now+lenW):
                    bold[k] = True # 逐格標示成 True
                now = s.find(word, now+1) # 往右繼續找word
        ans = [] # 串答案
        bolding = False # 記錄現在的狀態
        for i in range(N):
            if bold[i] and not bolding: # 變成 bold
                bolding = True
                ans.append('<b>')
            elif not bold[i] and bolding: # 變成不是 bold
                bolding = False
                ans.append('</b>')
            ans.append(s[i]) # 插入字母
        if bolding: ans.append('</b>') # 最後收尾
        return ''.join(ans) # 最後串答案
