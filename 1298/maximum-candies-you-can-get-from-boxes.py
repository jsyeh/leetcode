# LeetCode 1298. Maximum Candies You Can Get from Boxes
# n 個盒子 0...n-1， 分別由 status[i] candies[i] keys[i] containedBoxes[i] 
# 對應「盒子是否打開」、「糖果量」、「盒中有的鑰匙(能再開哪些盒子)」、「盒中有更多的盒子」
# 問最多能拿到多少糖果
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        N = len(status)  # 有 N 個盒子
        yourBox = set(initialBoxes)  # 你手上的盒子
        ans = []  # 你手上的盒子, 且它是打開的「在你手上、打開的盒子」
        for i in yourBox: # 檢查你手上的盒子
            if status[i]==1: ans.append(i)  # 它是「打開的」
        for i in ans:  # 針對「你手上、打開的盒子」逐一檢查
            for k in containedBoxes[i]:  # 檢查「盒子i」逐一取出裡面的「小盒子k」
                yourBox.add(k)  # 你多拿到一個小盒子
                if status[k]==1:  # 它是開的
                    ans.append(k)  # 又多了一個「在你手上、打開的盒子」
            for k in keys[i]: # 再檢查「盒子i」裡面的鑰匙 k 逐一測試
                if status[k]==0 and k in yourBox:  # 剛好你手上的「盒子k」還沒打開
                    ans.append(k)  # 又多了一個「在你手上、打開的盒子」
                status[k] = 1  # 這個盒子k「能打開了」以後能簡化「第15行」的程式
        return sum(candies[i] for i in ans)  # 統計「在你手上、打開的盒子」裡的糖果
