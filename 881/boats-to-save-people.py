# people[i] 是某人的體重，船有重量上限 limit，可裝1-2人
# 問要幾艘船，才能把全部的人載完
# 關鍵應該是「重的人」先上船，再看剩下能再載哪個輕的人
# 所以 sort() 後，便能用簡單的 two pointers + greedy 來解
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        left, right = 0, len(people) - 1  # 左右邊界
        while left <= right:  # two pointers 還沒交錯/還要載人
            if people[right] + people[left] <= limit:
                left += 1  # 可以多載一個瘦的人，就帶走
            right -= 1  # 每趟一定可載走一個重的
            ans += 1  # 每輪要多用一艘船
        return ans

