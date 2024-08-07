class Solution:  # LeetCode 273. Integer to English Words 用英文單字，表示數字
    def numberToWords(self, num: int) -> str:
        a = [0,1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90]
        b = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        table = dict(zip(a,b))
        def under1000(num):  # 只處理千位數以下的狀況
            ans = [] # 利用 list 來存放「單字」的字串（之後再用空白隔開）
            if num>=100:  # 有百位數
                ans.append(table[num//100])
                ans.append('Hundred')  # 就要有 'Hundred'
            num = num % 100  # 剩下2位數
            if num==0: return ans  # 簡單的 0 直接結束
            elif num<=20 or num%10==0:  # 20以下的數 or 10的倍數，有單字對應，可查表
                ans.append(table[num])
            else:  # 剩下的，就「幾十幾」的形式，來呈現
                ans.append(table[num//10*10])  # 十位數
                ans.append(table[num%10])  # 個位數
            return ans
        ans = []
        if num==0: return 'Zero'  # 遇到0的話，要特別處理： 'Zero'
        if num>=1000000000:  # 有 Billion 的等級
            ans += under1000(num // 1000000000)
            ans.append('Billion')
            num = num % 1000000000  # 剩下的數
        if num>=1000000:  # 有 Million 的等級
            ans += under1000(num // 1000000)
            ans.append('Million')
            num = num % 1000000  # 剩下的數
        if num>=1000:  # 有 Thousand 的等級
            ans += under1000(num // 1000)
            ans.append('Thousand')
            num = num % 1000  # 剩下的數
        if num>0:  # 如果還有剩，繼續
            ans += under1000(num)
        return ' '.join(ans)
