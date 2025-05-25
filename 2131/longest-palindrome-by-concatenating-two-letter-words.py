# LeetCode 2131. Longest Palindrome by Concatenating Two Letter Words
# 利用 words 裡「許多2個字母的字串」組合出「最長的Palindrom迴文」長度
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)  # 先將 words 裡的字，統計有哪些
        ans = 0  # 迴文的長度
        center = 0  # 中間若放「2個相同字母」，能貢獻嗎？
        for w in counter:  # 針對目前有的字
            if w[0]==w[1]:  # 2相同字母，可放迴文中間，也可與自己配對
                ans += counter[w] // 2 * 4  # 偶數的部分，可對稱放
                if counter[w]%2==1: center = 2  # 可放在中間的2個字母
            elif counter[w] > 0 and counter[w[1]+w[0]] > 0:  # 「反的字」存在，可搭配
                now = min(counter[w], counter[w[1]+w[0]])  # 可配出 now 組
                ans += 4 * now  # 左2個字母、右2個字母，共4個字母
                counter[w] -= now  # 用掉 now 個
                counter[w[1]+w[0]] -= now  # 用掉 now 個
        return ans + center  # 能組出「迴文」的最長長度
