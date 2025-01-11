# LeetCode 2981. Find Longest Special Substring That Occurs Thrice I
# 「只用1種字母」的連續substring，要出現3次。最長有多長？
class Solution:
    def maximumLength(self, s: str) -> int:
        counter = Counter()  # 利用 counter 來統計各種子字串長度（限定「只用1種字母」）
        for i,c in enumerate(s): # substring 開始位置i，對應字母c
            for j in range(i,len(s)): # substring 結束位置j，希望s[i]..s[j]都相等~
                if s[j]==c:  # 字母持續相等
                    counter[ (c,j-i+1) ] += 1  # （長度j-i+1)的子字串，數量+1
                else:  # 但若不幸不同時，就斷掉了
                    break  # 中斷 combo 就離開迴圈
        # 最後，統計答案
        ans = -1
        for (c,length) in counter:  # key 裡面放 (c, 長度)
            if counter[(c,length)]>=3:  # 若這種「子字串」出現3次以上，可再細看它的長度
                ans = max(ans, length)  # 想找「最長」的「只用1種字母」的子字串
        return ans
