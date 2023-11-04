class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:

        ans1, ans2 = 0, 0 # 還沒看到螞蟻, 先都是0

        # 有往右的螞蟻的話，最左邊的要走 n-min(right)
        if len(right)>0: ans1 = n-min(right)

        # 有往左的螞蟻，最右邊的要走 max(left)
        if len(left)>0: ans2 = max(left)

        return max(ans1, ans2)

