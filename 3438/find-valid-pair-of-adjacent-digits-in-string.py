# LeetCode 3438. Find Valid Pair of Adjacent Digits in String
# s 字串裡，每個數字有「出現次數」，找出「相鄰2數字/字母」不同，且出現次數，剛好是「那個」數字
class Solution:
    def findValidPair(self, s: str) -> str:
        counter = Counter(s)  # 利用 Counter() 統計出現次數
        for i in range(len(s)-1):
            a, b = s[i], s[i+1]  # 相鄰2字母
            if a==b: continue  # 字母不能相同哦
            if int(a) == counter[a] and int(b) == counter[b]:
                return a+b  # 對應的字母，出現的次數，剛好是「那個」數字
        return ""  # 都沒找到的話，回傳「空字串」
