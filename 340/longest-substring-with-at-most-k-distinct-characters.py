# 最多有k種不同字母的substring，最長有多長
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = collections.Counter()
        counterN = 0 # 加速用的，判斷「有幾種不同的字母」
        ans = 0
        left = 0
        for right in range(len(s)):
            counter[s[right]] += 1 # 統計有幾種不同的長度
            if counter[s[right]]==1: counterN += 1 # 加速用的
            while counterN>k: # 超過，就把尾巴縮短
                counter[s[left]] -= 1
                if counter[s[left]]==0: counterN -= 1 # 加速用的
                left += 1
            # 現在就是合法的長度
            ans = max(ans, right-left+1) 
        return ans
