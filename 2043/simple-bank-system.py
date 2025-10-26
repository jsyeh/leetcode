# LeetCode 2043. Simple Bank System
# 模擬「銀行」的資料結構，實作「轉帳、存款、提款」3種操作
# 小心：參數不對時 or 金額不足時，return False
class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.N = len(balance)
        # 陣列是 0-index 但 account 是 1-index

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1<1 or account1>self.N: return False
        if account2<1 or account2>self.N: return False
        if self.balance[account1-1] < money: return False
        self.balance[account1-1] -= money  # 要轉成 0-index
        self.balance[account2-1] += money  # 要轉成 0-index
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account<1 or account>self.N: return False
        self.balance[account-1] += money  # 要轉成 0-index
        return True
        
    def withdraw(self, account: int, money: int) -> bool:
        if account<1 or account>self.N: return False
        if self.balance[account-1] < money: return False
        self.balance[account-1] -= money  # 要轉成 0-index
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
