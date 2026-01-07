# LeetCode 859. Buddy Strings
# 如果把 s 的 2個字母交換後，會得到 goal 的話，return True
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False  # 長度不同，失敗
        if Counter(s) != Counter(goal): return False  # 內容不同
        # 相同的字串，若有2個相同的可交換，也叫成功
        if s == goal and max(Counter(s).values())>=2: return True
        # 若剛好有兩個不同，且「不同」的集合相同，叫成功
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(set([s[i], goal[i]]))
        if len(diff)==2 and diff[0] == diff[1]: return True
        return False
