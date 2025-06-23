# LeetCode 2081. Sum of k-Mirror Numbers
# k-mirror數: 正著讀、倒著讀，數字都一樣，而且 10進位、k進位都是。
# 因很少見，所以 數字會長得很快、很大。將前 n 項 k-mirror 數「加起來」
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def helper(x): # Hint 建議「產生palindrome」再檢查
            # 使用 Ye Gao 的方法, 從 x 出發，找下一個「k進位」字串迴文，比較巧妙、比較難
            for i in range(len(x)//2, len(x)):  # 切一半的「位數」開始「往右試」
                # ex. 12321 的 123 試 124 看看
                if int(x[i])+1 < k:  # 下一項「還沒有(k進位的)進位」，可試
                    x[i] = x[-i-1] = str(int(x[i])+1)  # 左右兩位都+1
                    for ii in range(len(x)//2, i):
                        x[ii] = x[-ii-1] = '0'  # 把「低位數」都「左右對稱」變成0
                    return x
            return ['1'] + ['0']*(len(x)-1) + ['1']  # 無法找到，「再多1位」
        x = ['0']  # 用字串來產生「迴文」
        ans = 0  # 後面利用 for 迴圈找「前n項」，裡面用 while迴圈判斷10進位迴圈，比較簡單
        for i in range(n):  # 要找「前n項」
            while True:  # 用 while 迴圈，試到找出下一項
                x = helper(x)  # 用 helper()找k進位迴文的候選人
                now = int("".join(x), k)  # 把k進位字串變整數
                if str(now) == str(now)[::-1]:  # 也是10進位迴文
                    break  # 找到第i筆答案，離開 while 迴圈
            ans += now  # 將答案「加起來」
        return ans  # 順利找到「前n項」加起來的答案
'''
今天 2081 題目先定義 k-mirror 數字的意思：這個數，不管是在10進位 or k進位，都是「正著讀、反著讀」都相同的迴文。請你找出「前n項」k-mirror 的數，再把它們「加起來」。

題目輸入的數很小，但因為 k-mirror 的條件很難達成，所以「數字會成長很快」變得超級大，所以題目input的 k<=9 及 n<=30 但還是有點難。題目 Hint 建議「用產生 palindrome」 的方式來解這題，讓 search space 變小，才不會太慢。

這題也是超過我理解範圍的題目 --- 沒有多做掙扎，我就先參考了 Vlad 及 Ye Gao 及 Editorial 的解法，使用的方法，分別是「先產生10進位的迴文」再檢查、「先產生k進位的迴文」再檢查、「binary search 再 暴力列答案法」。裡面 Ye Gao 的程式最短，我就看他的答案。

Ye Gao 「先產生k進位迴文」的解法策略：很巧妙的 helper()函數，從「前一項」字串list出發，先「剪刀剪一半」，以「左右對稱」的原則，看「哪一項可以+1」不會碰到 k 進位的上限，就把它「左右對稱都+1」，再把最比較小的其他項「都變成0」 --- 若都找不到「能+1」的位置，就變出類似 10001 增加1位數。這部分比較巧妙、比較難。

有了 helper()幫忙，再配合 for 迴圈及 while 迴圈，找到「10進位也是迴文」的「前n項」加起來，就是答案。後面這個部分相對簡單。祝大家 LeetCode 快樂！
'''
