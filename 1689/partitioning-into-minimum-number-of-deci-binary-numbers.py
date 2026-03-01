# LeetCode 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
# 需要「幾個二進位字串」，假裝「像10進位加法」，加起來是n。
class Solution:
    def minPartitions(self, n: str) -> int:
        # 經觀察，就直接找到「字串裡」最大的數即可
        return int(max(list(n)))
