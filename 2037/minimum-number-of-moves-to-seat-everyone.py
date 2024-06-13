# LeetCode 2037. Minimum Number of Moves to Seat Everyone
# students 要移到 seats 總共要移幾步？
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()  # 先排序
        students.sort()  # 先排序
        ans = 0
        for i in range(len(seats)):  # 照順序，走到位置坐下來
            ans += abs(seats[i]-students[i])  # 要移動的距離
        return ans
