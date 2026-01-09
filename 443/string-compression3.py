# LeetCode 443. String Compression
# 字串壓縮時，長度1的字母「不用加數字」，其他要加數字。
# 將「壓縮後的字串」逐一放回 chars 並回傳「壓縮後」字串長度
class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 1  # 「壓縮後」的長度, 且「壓縮後」的字串放在 chars
        prevN = 1  # 前一項的字母、重覆的次數。一開始是1個字母
        for i in range(1,len(chars)+1):
            if i<len(chars) and chars[i]==chars[ans-1]:  # 字母相同
                prevN += 1  # 多1個字母
            else:  # 字母不相同
                if prevN > 1:  # 很多，便用「數字」壓縮
                    for c in str(prevN):  # 把「數字」變字母
                        chars[ans] = c  # 依序塞入
                        ans += 1
                prevN = 1
                if i<len(chars):  # 還有新的字母
                    chars[ans] = chars[i]  # 把新字母塞入
                    ans += 1
        return ans

