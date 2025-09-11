# LeetCode 1733. Minimum Number of People to Teach
# n種語言、m個人，languages[i] 對應 user i 會使用的語言。
# friendships[i] = [u,v] 代表 u 和 v 是「好朋友」、可互相溝通。
# 你挑一種語言來教學，需要教幾個人後，「好朋友」就可以互相溝通？
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # 陣列原本是 0-index 從0開始，改成題目講的 1-index 從1開始
        # 只要在最前面「插入一坨東西」就可以變 1-index
        languages.insert(0, [])  # 先變成 1-indesx
        # 任務一：把每個人會的語言，都變成 set()
        for i in range(len(languages)):
            languages[i] = set(languages[i])
        # 任務二：找出「無法溝通」「需要幫忙的好朋友」
        need_help = []  # 需要幫忙的「好朋友」有哪些組？
        for u,v in friendships:
            if languages[u] & languages[v] == set():  # 交集的結果是「空」表示需要幫忙「教新語言溝通」
                need_help.append( [u,v] )
        # 任務三：嘗試教「無法溝通」的好朋友「語言L」
        ans = inf
        for L in range(1,n+1):
            helped = set()  # 教了哪些人、幫了哪些人
            for u,v in need_help:
                if L not in languages[u] and u not in helped: helped.add(u)
                if L not in languages[v] and v not in helped: helped.add(v)
            ans = min(ans, len(helped))  # 更新答案
        return ans
