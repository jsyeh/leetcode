# LeetCode 3306. Count of Substrings Containing Every Vowel and K Consonants II
# 在 word 裡，有幾個 substring 剛好全部母音 vowel 和k個子音 consonants
# 可用「毛毛蟲」來「收集全部母音」及k個子音。但「剛好k個子音」不好做，改用 helper(k) 找 k以上的子音
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def helper(k):  # 希望找到 k 個以上的子音，有幾種？
            counter = Counter()  # 統計各種母音「有幾個」
            vowel = set(list("aeiou"))  # 快速找「母音」的 set()
            other = 0  # 不是母音的「子音」有幾個
            ans = 0
            tail = head = 0  # 左邊尾巴（吐字母）、右邊是頭（吃字母）
            N = len(word)
            while tail < N and head <= N:  # 還可以吃、可以吐哦！
                if len(counter)==5 and other>=k:  # 收集齊了5種母音 & k個以上的字音
                    # 7顆龍珠出現，可以許願
                    ans += N - head + 1  # 頭的右邊，有更多的字母可以吃，都是「k個以上」
                    c = word[tail]  # 左邊要吐掉的字母
                    if c in vowel:  # 母音
                        counter[c] -= 1
                        if counter[c] ==0: del counter[c]  # 此母音消失囉
                    else:  # 子音
                        other -= 1
                    tail += 1  # 左邊尾巴吐掉，右移1格
                else:  # 沒有收集齊7顆龍珠，就右邊繼續吃
                    if head==N: break  # 到底了、不能再吃了，結束！
                    c = word[head]
                    if c in vowel: counter[c] += 1  # 母音
                    else:  other += 1  # 子音
                    head += 1
            return ans
        return helper(k) - helper(k+1)  # k以上有幾個 - (k+1)以上有幾個 == 剛好有 k 個
