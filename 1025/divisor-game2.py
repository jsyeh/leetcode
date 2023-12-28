# 「除法運算」的遊戲, 找出可以整除n的數x, 再把n = n-x
# 不能再找到數字的話, 就輸了。請問 Alice 會不會得勝
# 就用「函式呼叫函式」來解決即可
class Solution:
    def divisorGame(self, n: int) -> bool:
        # 但是沒想到, 有人利用 recursion證明, 只要 return n%2==0 即可, 真可惡!
        return n%2==0
