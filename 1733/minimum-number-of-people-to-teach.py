# LeetCode 1733. Minimum Number of People to Teach
# n種語言、m個人，languages[i] 對應 user i 會使用的語言。
# friendships[i] = [u,v] 代表 u 和 v 是好朋友、可互相溝通。
# 你能挑一種語言、教幾個人後，「好朋友」就可以互相溝通？
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        M = len(languages)  # 有 M 個人，要建立它們的語言 set()
        for i in range(M):  # 把「每一個人」會的語言
            languages[i] = set(languages[i])  # 都變成 set()，方便「交集」語算
        bad = [] # 找出 沒有「share相同語言」的組（需要幫忙）
        for u,v in friendships:  # u 和 v 兩人「需要當好朋友」
            # print(u,v) # 小心，題目的 u,v 從1開始 1-index
            if languages[u-1] & languages[v-1] == set():  # 交集「空」
                bad.append( [u-1,v-1] )  # 記下這一組，同時轉成 0-index
        ans = inf
        for L in range(1,n+1): # 你這次「嘗試教L語言」讓無法溝通的朋友「溝通」
            now = set()  # 這次你將要教的學生(教過的，就不用再教)
            for u,v in bad:  # 無法溝通的這組朋友，你將要教他們 L 語言
                if L not in languages[u] and u not in now: now.add(u)  # 需要教
                if L not in languages[v] and v not in now: now.add(v)  # 需要教
            ans = min(ans, len(now))
        return ans
