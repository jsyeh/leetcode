# LeetCode 3343. Count Number of Balanced Permutations
# 數字的字串「隨便你排組合」能湊出幾個 balanced (sum奇數位 == sum偶數位) 的數
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        @cache  # 參考 Vlad 的解法，利用「函式呼叫函式」來解
        def helper(d, odd, even, balance):  # 現在處理數字 d (依序9...0處理)
        # 現在處理數字d，奇數、偶數位「各剩幾位」要填，奇數位「還需放多少」
            if odd==0 and even==0 and balance==0:
                return 1  # 剛好奇偶（位數）排完，剛好odd把它的一半用完，得到1組解
            if d<0 or odd<0 or even<0 or balance<0:  # 任一個用過頭（變負）
                return 0  # 不幸走入死胡同，無法湊出解
            ans = 0
            dN = counter[d]  # 現在處理的 digit d 的數量 有 dN 個，左右分配
            for k in range(dN+1):  # 給 odd k 個，給 even (dN-k) 個
                now = helper(d-1, odd-k, even-(dN-k), balance-d*k)  # 照此分配，往下做
                ans += comb(odd, k) * comb(even, dN-k) * now  # 排列組合：挑奇數位、挑偶數位
            return ans % 1000000007  # 排列組合後的可能太大, 記得取餘數 10^9+7

        nums = [int(c) for c in num]  # 先把「字串」變成「數的陣列」
        counter = Counter(nums)  # Hint 1 建議數一數「出現頻率」
        total = sum(nums)  # 每一位數加起來
        if total%2==1: return 0  # 「加起來」是奇數，就無法「平均分配」
        even = len(num) // 2  # num 裡，有一半的偶數位數（無條件捨去）
        odd = len(num) - even  # 剩下的是奇數位 ex. "123" 奇數位有2位
        return helper(9, odd, even, total//2)  # 從數字 9 「開始倒數」
