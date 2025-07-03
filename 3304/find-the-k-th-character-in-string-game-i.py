# LeetCode 3304. Find the K-th Character in String Game I
# 字串產生的規則: 每複製一倍、子母換下一個字母、接到後面。
# 照此生成規則，找出第 k 個子母。一開始想用「函式呼叫函式」來解，但總差一點
# 後來試了一些數 1...11後,突然發現規律:和幾個1有關係
# 4->2->1 8->4->2->1, 6->2->1
# 5->1 好像有幾個1就升級幾次，不過需要先轉成 0 開始
class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = 0
        k -= 1  # 從人類習慣的 1-index 變成電腦的 0-index
        while k>0:  # 用剝皮法，數一數「有幾個1」
            ans += k%2  # 剝皮法
            k //= 2  # 剝皮法
        return chr(ord('a')+ans%26)  # 最後把位移量 %26 再轉成字母即可
