# LeetCode 157. Read N Characters Given Read4
# 你可使用 read4() 讀入 4 個字母，放到 buf4 裡
# 利用 read4() 來讀入 n 個字母
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        ans = 0  # 累積的答案長度
        for i in range(0, n, 4):
            buf4 = [' '] * 4
            revl = read4(buf4)
            buf[i:i+revl] = buf4[:revl]  # 將 list 的內容替換掉
            ans += revl  # +順利讀到的長度
        return min(n, ans)  # 看哪個比較少，便是正確的長度
