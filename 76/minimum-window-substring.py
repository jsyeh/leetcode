class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterT = Counter(t) # target 目標的統計表
        counterNow = Counter() # 目前統計表(空)，毛毛蟲在爬會改變內容

        # 下面這個迴圈沒有效率，會讓第20行 while enough() 變慢
        def enough(): # 現在收集的 counterNow[] 夠用嗎？
            for c in counterT: # 希望目標裡，每個數量都達標
                if counterNow[c] < counterT[c]: # 收集不夠
                    return False # 失敗
            return True # 全部都夠用，就成功

        ansI, ansJ, ansLen = 0, 0, inf # 答案的毛毛蟲：頭、尾、長度
        i, j = 0, 0 # 現在正在爬的毛毛蟲的左邊i 右邊j
        N = len(s) # 毛毛蟲的迴圈要用到N
        while j<N: # 右邊j沒超過範圍
            counterNow[ s[j] ] += 1 # 右邊往右，吃到 s[j] 字母
            j += 1 # 往右爬

            while enough(): # 夠用，讚，繼續更新，等下左邊i會吐出來
                if (j-i) < ansLen: # 更短的話
                    ansI, ansJ, ansLen = i, j, j-i # 更新答案
                counterNow[ s[i] ] -= 1 # # 夠長嘛，左邊i可再吐出來
                i += 1 # 左邊尾巴右移
        if ansLen == inf: return '' # 沒有答案(無限長)
        else: return s[ansI:ansJ]
