# 最多只能有2種字母 的連續substring，最長多長？
# 就使用 two pointers 應該就可以了
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        usedSet = set() # 裡面放「使用的字母」
        usedDict = defaultdict(int) # 字母出現次數
        i, j = 0, 1 # 左包含, 右不包含
        usedSet.add(s[0])  # 最前面第1個字母
        usedDict[s[0]] += 1 # 它出現1次

        N = len(s)
        ans = 1
        while i<j and j<N: # 要攞放正確（左手i 右手j）
            usedSet.add(s[j])
            usedDict[s[j]] += 1
            j += 1
            while len(usedSet)>2: # 超過的話，要一直縮
                usedDict[s[i]] -= 1 # 左邊吐出1字
                if usedDict[s[i]]==0: # 如果為0
                    usedSet.remove(s[i]) # 可以少1個
                i += 1 # 吐完後，i右移
            ans = max(ans, j-i) # j-i 便是長度
        return ans
