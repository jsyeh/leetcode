# LeetCode 1639. Number of Ways to Form a Target String Given a Dictionary
# 題目觀念不難，但因「測試資料」太大、太難，導致程式需要一直修正。最後我使用 lee215 的概念，省下大量迴圈
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        M, N = len(words), len(words[0])
        MOD = 10**9+7  # 答案會太大，需要取 MOD 餘數
        counter = [Counter() for k in range(N)] 
        for word in words:  # 統計 words[i] 每個位置 k 的各種字母 c「出現幾次」，用來「乘出」答案
            for k, c in enumerate(word):
                counter[k][c] += 1  # words[i] 第 k 個字母是 c 的次數
        @cache
        def helper(i, k):  # target[i] 的字母，是不要用 word[j][k] （words[j]的第 k 個字母）
            if i == len(target): return 1  # 成功組出 target
            if k == N: return 0  # 字母耗盡，但沒成功
            c = target[i]  # 現在要處理的字母是 c 
            ans1 = helper(i, k+1)  # 不使用第k個字母，能達成任務，有幾種可能
            ans2 = helper(i+1, k+1)  # 使用第k個字母，繼續處理下一個字母，有幾種可能（等一下要再乘上 counter[k][c]）
            return ( ans2 * counter[k][c] + ans1 ) % MOD
        return helper(0, 0)
        # 下面的程式碼=====請不要看、請不要看、請不要看、請不要看、請不要看、請不要看、請不要看、請不要看=====
        # 下面的解法，還是會 TLE 超時，因為要逐個處理 words[j] 的字母
        @cache
        def helper(i, k):  # 要組合 target[i]，用words[j][k]之右的字母
            if i == len(target): return 1
            if k == N: return 0
            ans = 0
            for j in range(M):
                for kk in range(k, N):  # 可能會超過時間
                    if words[j][kk]==target[i]:  # 找到字母
                        ans += helper(i+1, kk+1)
            return ans % MOD  # 答案會太大，需要取 MOD 餘數
        return helper(0, 0)
# case 75/90 TLE
# case 47/90 會出錯，因為 MOD

        # 下面解法，是針對「每個words[j]都有自己」「用過後不可回頭」的特質
        # 但此題沒那麼難，用上面的「大家共用k」「用過後不可回頭」，才是對的
        @cache
        def helper(i, usedIndex):
            if i==len(target): 
                print('good', usedIndex)
                return 1
            ans = 0
            usedIndex2 = list(usedIndex)
            for j in range(M):
                for ii in range(usedIndex[j],N):  # 可能會超過時間
                    if words[j][ii] == target[i]:
                        usedIndex2[j] = ii+1
                        print(usedIndex2, 'use', ii, target[i])
                        ans += helper(i+1, tuple(usedIndex2))
                        usedIndex2[j] = usedIndex[j]
            return ans % MOD
        usedIndex = [0]*N
        return helper(0, tuple(usedIndex))

        
