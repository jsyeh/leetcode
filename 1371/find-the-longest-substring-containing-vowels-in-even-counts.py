# LeetCode 1371. Find the Longest Substring Containing Vowels in Even Counts
# 希望「每一個母音」都有「偶數個」，找符合的最長字串
# 有點像使用 prefixSum 的技巧，能找到「某堆奇偶組合」最早前的位置，利用 bitMask 來找
# 邊讀、邊更新「奇偶組合」，找到「第1次出現的位置」，位置相減，便是「最長」的距離，再「更新」答案
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowelBit = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16 }  # bitMask 對表表
        ans, now = 0, 0  # now 是現在的 bit 「奇偶組合」
        firstPos = [-1]*(2**5)  # 5個bits，有2^5 種可能，放-1代表還沒出現過
        for i,c in enumerate(s): # 第i個字母 s[i] 是 c
            if c in vowelBit:  # 是「母音」
                now ^= vowelBit[c]  # 用 XOR flip 切換「對應bit」的值
            if firstPos[now]==-1 and now!=0:  # 之前沒出現過，不能是0(特殊的起始值)
                firstPos[now] = i  # 記下「第1次出現」的位置
            else: # 之前有出現過，就可更新答案
                ans = max(ans, i - firstPos[now])  # 現在位置 - 前次出現位置，對應「最長」字串長度
        return ans
            

