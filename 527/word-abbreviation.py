# LeetCode 527. Word Abbreviation
# 把 like 變 l2e, intension vs. intrusion 就多些字母，變 inte4n 及 intr4n
# 但 internal vs interval 縮寫一樣，沒有縮寫必要，就留原字
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        # 可把 words 先簡化，遇到「重覆」就「再變長一些」，參考 Editorial 解法
        def helper(word, i):  # 簡化：頭尾保留、再保留i個字母
            if len(word) - i <= 3: return word  # 無法再縮寫
            return word[:i+1] + str(len(word) - i - 2) + word[-1]

        ans = [ helper(word, 0) for word in words ]
        nn = [0 for word in words]  # nn[i] 對應 words[i] 額外保留的「字母」
        for i in range(len(words)):  # 逐字比較
            while True:  # 一直持續做簡化
                bad = set()  # 下面迴圈「有重覆」的嗎？
                for j in range(i+1, len(words)):  # word[i] vs. word[j] 
                    if ans[i] == ans[j]:  # 「縮寫」有重覆，就要處理
                        bad.add(j)  # 會和 words[i]重覆的，全記起來「等待處理」
                if len(bad)==0: break  # 沒有任何重覆，很好，可換下個字母 i+=1
                bad.add(i)  # words[i] 也要一起「等待處理」
                for ii in bad:  # 把所有「等待處理」的，都一起變長
                    nn[ii] += 1  # 多保留1個字母
                    ans[ii] = helper(words[ii], nn[ii])
        return ans
