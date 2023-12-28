# 「除法運算」的遊戲, 找出可以整除n的數x, 再把n = n-x
# 不能再找到數字的話, 就輸了。請問 Alice 會不會得勝
# 就用「函式呼叫函式」來解決即可
class Solution:
    @cache
    def divisorGame(self, n: int) -> bool:
        # 先把全部「可以整除」的因數都找出來, 再逐一測試
        if n==1 or n==0: 
            return False # 無法找到 0 < x < n 就輸了
        if n==2: return True # 已知可win

        for now in range(1,int(n**0.5)+1):
            if n%now==0 and self.divisorGame(n-now)==False: 
                # 可整除, 且 挑now可讓對方輸
                return True # 就挑它now 即可
        return False # 找不到可以win的機會, 這輪應該是輸了
# case 3/40: 4 可自己多試一些測資
