# 依序將A，B移除，移除時，必須要連續3個才行。
# 所以，就數「有幾個連續大於3」的數目，再比大小，即可知答案
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        H = {'A':0, 'B':0}
        for i in range(1, len(colors)-1):
            if colors[i-1]==colors[i] and colors[i]==colors[i+1]:
                H[colors[i]] += 1 # 有連續3個，就得1分
        
        # A > B 就是 A 勝
        if H['A'] > H['B']: # 不能等於，因為A無法先手，A就敗
            return True
        else:
            return False

# case 81/83: "AAAABBBB"
