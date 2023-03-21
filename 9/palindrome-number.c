//Week06-2.cpp 解 LeetCode 的程式
//不是寫完整的程式, 只要寫一個函式
//判斷迴文, 要用到的程式技巧: 使用 for迴圈, if判斷, while迴圈
bool isPalindrome(int x){
    int x2 = x; //備份x到x2
    //很長很長的整數
    long long int r = 0; //反過來的數字, 等一下要放在 r裡面
    while( x > 0 ){
        //很長很長的整數
        r = r*10 + x%10; //剝皮
        x = x / 10;
    }
    //使用剝皮法
    //最後x剝完,變成0...完了 x不能用
    if(x2 == r) return true;
    else return false;
}
