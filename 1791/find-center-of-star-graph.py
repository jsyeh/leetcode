# LeetCode 1791. Find Center of Star Graph 好久沒出現 Easy 題了哦! 
# 好開心! 給一堆 edges 裡面會重覆出現的叫 center。把 center 找出來。
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]  # 兩個當中, 一定有一個是 center
        if edges[1][0] == a: return a
        if edges[1][1] == a: return a
        if edges[1][0] == b: return b
        if edges[1][1] == b: return b
        # 用很笨的方法, 去試看看, 到底誰重覆了。重覆的那個, 就是 center
