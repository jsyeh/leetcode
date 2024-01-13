# 有些列在 words 裡的字母，要標示成 <b>...</b> 粗體字
# 且不要「重覆標示」
# 所以要在 s 裡「找出這些字」，又 s長度<=500 可用陣列來標示
class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        N = len(s) # 字串長度，方便檢查時「省時間」
        bold = [False]*N # 標示是否是「粗點字」
        for i in range(N): # 開始的座標
            for word in words: # 待測的字
                if word == s[i:min(N,i+len(word))]: # 比較切下的字
                    # 這裡暴力比對，比較沒有效率。之後可用trie加束
                    for k in range(i,i+len(word)):
                        bold[k] = True # 字相同，就逐格標不
        ans = [] # 用來存字，等下會 ''.join()起來
        print(bold)
        bolding = False # 正在粗體字中 --- 可避免重覆標示
        for i in range(N):
            if bold[i] and not bolding: # 要變成 bolding
                bolding = True
                ans.append('<b>')
            elif bolding and not bold[i]: # 要變「不是bolding」
                bolding = False
                ans.append('</b>')
            ans.append(s[i])
        if bolding: # 在字串收尾時，也要記得「收尾」
            ans.append('</b>')
        return ''.join(ans)
# case 39/27: ["ccb","b","d","cba","dc"] "eeaadadadc"
# 在字串收尾時，也要記得「收尾」
