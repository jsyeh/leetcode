# 這題很像是「模擬比賽對決」的晉級模擬。偶數要對戰 n//2 場, 奇數則是 (n-1)//2 場
# 持續比, 直到冠軍出來。
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n>1: # 還沒有確認冠軍那1隊
            if n%2==0: # 偶數
                ans += n // 2 # 這次要對決 n//2 場
                n = n // 2 # 這次剩下的隊伍
            else: # 奇數
                ans += (n-1) // 2 # 這次要對決 (n-1) // 2 場
                n = n //2 + 1 # 剩下的隊伍
        return ans # 總共對決matches的次數
