# 問「有幾組」不同的 email address
# 其中 name@domain.com 的 name 裡的句號，可以省略/當成相同的
# 而 name+ooxx@domain.com 與 name@domain.com 是相同的
# 所以要處理 . 與 +
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails: # 題目保證 email 必有1個'@'
            name, domain = email.split('@') # 前後斷開
            name = name.replace('.','')
            name = name.split('+')
            name = name[0]
            now = name+'@'+domain
            ans.add(now)
        # print(ans)
        return len(ans)
