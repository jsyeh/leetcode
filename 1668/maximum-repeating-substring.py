# LeetCode 1668. Maximum Repeating Substring
# 這題好難想。Solutions 有人用迴圈暴力做(測不同長度），就簡單了
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        repeat = word
        while repeat in sequence: 
            ans += 1
            repeat += word
        return ans
