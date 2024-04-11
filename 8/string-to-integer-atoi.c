// 同學好奇我怎麼解這題。之前曾用 C++ 和 Python 寫過, 這次就用C試試看
// 先解決 leading zero 的問題
// 再處理 + - 正負號的開頭
// 接著遇到數字時, 以10進位方式, 逐項變大。
//  但超過 INT_MIN 或 INT_MAX 時, 提早輸出
int myAtoi(char* s) {
    int leading_space = 0, sign = 0;
    for(int i=0; s[i]!=0; i++){ //字串的迴圈
        if(s[i]==' ') leading_space++; //先處理 leading space 前面的空格
        else break; //如果沒有空格, 就結束leading space的處理
    }
    if(s[leading_space]=='+') leading_space++; //正號, 避開這一格
    else if(s[leading_space]=='-'){ //負號
        sign = 1; //記得是負號
        leading_space++; //再避開這一格
    }
    long long int ans = 0; //因為 32bit 但在轉換時怕 overflow, 所以用 32bit
    for(int i=leading_space; s[i]!=0; i++){ //字串的迴圈, 從剛剛位置繼續
        if(s[i]>='0' && s[i]<='9'){ //數字
            ans = ans * 10 + s[i] - '0'; //照10進位的倍數乘上去
        }else break; //不是數字,就離開(空格也會離開哦)
        if(sign==1 && -ans<INT_MIN) return INT_MIN; //陷阱, 負太大的數, 只能是INT_MIN
        if(sign==0 && ans>INT_MAX) return INT_MAX;  //陷阱, 正太大的數, 只能是INT_MAX
    }
    if(sign==1) return -ans; //有負數
    return ans;
}
