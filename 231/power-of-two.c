// 測試 n 是不是 2^x。
// 2^0 是1， 所以要測到1為止
bool isPowerOfTwo(int n) {
    if(n<=0) return false; // 遇到負數 or 0，都是失敗
    while(n>1){ // 要測到1為止
        if(n%2!=0) return false; // 不是2的倍數，就失敗
        else n = n / 2; // 數字越除越小
    }
    return true; // 通過檢查，是 true
}
