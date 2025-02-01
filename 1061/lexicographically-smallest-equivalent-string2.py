# LeetCode 1061. Lexicographically Smallest Equivalent String
# s1 s2 的對應字母相同，即 s1[i] 和 s2[i] 的字母是「等價」
# 把 baseStr 變成「對應等價」的最小字母的字中
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        table = {chr(i):chr(i) for i in range(ord('a')+26)}
        # 先做出 26 個字母的對照表，每個字「先對應自己本身」（即26個group)
        def find(c):  # 想找到 c 等價的的最小字母
            if table[c] == table[table[c]]:  # 繞口令：最小的最小，還是最小
                return table[c]
            table[c] = find(table[c])  # 函式呼叫函式，找最小的最小
            return table[c]
        for i in range(len(s1)):
            c1, c2 = s1[i], s2[i]  # 對應字母，將會等價
            c1, c2 = find(c1), find(c2)  # 對應的最小
            c = chr(min(ord(c1),ord(c2)))
            table[c1] = table[c2] = c
        ans = []
        for c in baseStr:  # 逐一查表，建出 baseStr 對應的「等價最小字串」
            ans.append(find(c))
        return ''.join(ans)
