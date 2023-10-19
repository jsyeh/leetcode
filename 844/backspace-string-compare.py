# 這個題目超簡單: 在字串裡找到 '#' 出現的地方, 刪除它及它前面的字母。
# 如果#在最前面, 就只要刪掉它,因為它前面的字母不存在、沒辦法刪。
# 題目有希望 O(1) 的空間, 但 Python 沒辦法改 str 字串裡面的字母。
# 為了簡單解決, 我決定還是浪費一堆 memory吧, 把 s, t 都變成 list
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s, t = list(s), list(t) # 改用 list 來放值
        k = 0 # s[k] = s[i] 的想法
        for i in range(len(s)):
            if s[i]!='#':
                s[k] = s[i] # 簡單搬移過去 s[k]
                k += 1 # 到下一格待命
            else:
                k = max(k-1, 0) # 往左移,但不要變成負的
        k2 = 0
        for i in range(len(t)):
            if t[i]!='#':
                t[k2] = t[i] # 簡單搬移過去 t[k2]
                k2 += 1 # 到下一格待命
            else:
                k2 = max(k2-1, 0) # 往左移,但不要變成負的
        if s[:k] == t[:k2]:
            return True
        else:
            return False
