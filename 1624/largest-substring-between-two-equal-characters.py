# LeetCode 1624. Largest Substring Between Two Equal Characters
# 「夾在」兩相同字母「中間」的字母「最長」有幾個，像 abca 就是 2
# 另外像 aaaa 最左邊的a、最右邊的a 中間夾了 2個字母
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        left = {}  # 字母c 第一次出現的位置在 left[c]
        ans = -1 # 相知道相同字母的「最遠距離」,找不到就-1
        for i in range(len(s)):
            c = s[i] # 這次的字母
            if c not in left: # 第一次出現的話
                left[c] = i # 記得它（最左邊）的出現位置
            else: # 若之前出現過，可算最左邊vs現在的間隔距離
                ans = max(ans, i-left[c]-1) # 最大間隔距離
        return ans
# case 9/54: "mgntdygtxrvxjnwksqhxuxtrv"
