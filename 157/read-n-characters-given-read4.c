// LeetCode 157. Read N Characters Given Read4
// 你可使用 read4() 讀入 4 個字母，放到 buf4 裡
// 利用 read4() 來讀入 n 個字母，
/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

/**
 * @param buf Destination buffer
 * @param n   Number of characters to read
 * @return    The number of actual characters read
 */
int read4(char* buf); // 要自己「定義函式」才能成功送出程式
int _read(char* buf, int n) {
    int ans = 0; // 目前讀到幾個字母
    for(int i=0; i<n; i+= 4){
        int revl = read4(buf+i);
        ans += revl;
    }
    buf[n] = 0; // 要自己做「字串結尾」
    return ans;
}
// case 31/46: file="leetcode" n=5
// 不能讀到8個字母，要自己把字母結束
