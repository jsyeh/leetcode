# LeetCode 1061. Lexicographically Smallest Equivalent String
# s1 s2 的對應字母相同，即 s1[i] 和 s2[i] 的字母是「等價」
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        group = defaultdict(set)  # group 裡，會放 s1 vs s2 的「等價」字母資訊
        for i in range(len(s1)):
            group[s1[i]].add(s2[i])
            group[s2[i]].add(s1[i])
        # 接下來，從 group 出發，整理出「最小字母」的對照表
        def findSmallest(c):  # 利用「函式呼叫函式」找最小字母
            ans = c  # 若沒有其他等價對應，那自己會對應「自己」
            for d in group[c]:  # 如果有其他「等價」的資訊
                if d not in visited:  # 如果沒走過，就查看更新
                    visited.add(d)  # 先標註走過，避免重覆
                    now = findSmallest(d)  # 再進行「函式呼叫函戈心戈一」
                    if ord(now)<ord(ans): ans = now  # 若字母更小，就換更小的字母
            return ans  # 對應「最小」的等價字母
        table = {chr(i):chr(i) for i in range(ord('a')+26)}  # 完整對照表，先「自己對應自己」
        for c in group:  # 若有等價字母
            visited = set(c)  # 避免重覆進入的 visited set
            table[c] = findSmallest(c)  # 函式呼叫函式，更新「最小」的字母
        ans = []
        for c in baseStr:  # 針對問題，逐字母查詢
            ans.append(table[c])  # 放入「最小」的等價字母
        return ''.join(ans)  # 變回字串，回傳答案
