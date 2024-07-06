# LeetCode 2582. Pass the Pillow
# 有n個人，站在1...n的標籤前面。第1個人手上拿著枕頭，慢慢往後傳。
# 每秒傳1個人，左邊傳到右邊後，右邊再傳到左邊。問time時間時，枕頭在哪裡
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # n個人，從最左邊傳到右邊，再傳回來，需要2*(n-1)秒
        ans = time % (2*(n-1)) # 取餘數後，便將重覆的循環扣掉，剩下最後不到一輪
        if ans >=n: ans = (2*(n-1))-ans # 到達右界後，往左走幾個？現在到哪裡？
        return ans + 1 # 因為 label 是 1-index 所以要+1

