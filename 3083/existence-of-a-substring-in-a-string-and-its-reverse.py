# LeetCode 3083. Existence of a Substring in a String and Its Reverse
# 只要有「substring」及「它的反過來的substring」就是 True
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        # 我想到一招：就將「兩兩相鄰字母」記在 set裡
        # 巡一次時，如果有重覆「反過來」的，就是成功
        repeat2 = set()
        for i in range(len(s)-1): # 兩兩一組巡
            repeat2.add(s[i]+s[i+1])
            if s[i+1]+s[i] in repeat2: return True # 有找到
        return False  # 沒有找到

# case 714/718: "leafbcaef" 有 ea 及 ae
