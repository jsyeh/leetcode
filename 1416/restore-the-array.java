class Solution {
    public int numberOfArrays(String s, int k) {
        //int [][] table = new int[][k+1];//k很大不可
        //0會是斷字的重點，因0太多可能造成錯誤
        //if(checkZeroBad(s,k)==1) return 0;
        int N = s.length();
        int [] table = new int[N+1]; //table[i] 表示第i個字之後的可行的答案數
        dp(table, 0, s, k); //從 table[0]開始發動找答案
        return table[0];
    }
    int dp(int[] table, int start, String s, int k) {
//System.out.println(start);
        if(start >= s.length()) return 1;//最後超過邊界時，就是"" 空字串這個答案，不要去查陣列
        if(table[start]!=0) return table[start];//已經有找到答案，就送出
        if(s.charAt(start)=='0') return 0;//數字開頭不能是0，所以以下不可能，直接return 0;

        int total = 0;
        for(int end=start; end<s.length(); end++){ //start...end對應的字串，右邊界包念
            String substr = s.substring(start, end+1);//substring()右不含
            long now = Long.parseLong(substr);//參考答案寫 Long.parseLong() 不過我覺得 Integer.toInt()應也可以,但若k=823924906時，就會出錯，所以要用 long 才夠
            if(now>k) break;//因題目說 切 數字時，不能超過 k, 所以後面就不要再算了
            total += dp(table, end+1, s, k);//現在的切割法是合法的，那再細問 sub-problem
            total %= 1_000_000_007;
        }
//System.out.println(start + " total: " + total);
        table[start] = total;
        return total;
    }
    //case 30/83: "600342244431311113256628376226052681059918526204"
    //703
    //case 69/83: "407780786171321121429620765476840275495357129574174233567552131453038760763182952432348422252546559691171161181440370120987634895458140447952079749439961325982629462531738374032416182281868731817661954890417245087359968833257550123324827240537957646002494771036413572415"
    //823924906
    /*//我本來想先分析有幾個0，不過寫完後突然沒有靈感，所以偷看詳解。
    //覺得詳解的概念很好，想學起來，所以照著它的概念寫寫看
    int checkZeroBad(String s, int k) {
        int prev = s.charAt(0)-'0';
        int biggest = prev;
        for(int i=1; i<s.length(); i++){
            int now = s.charAt(i)-'0';
            if(now==0){
                prev = prev*10+now;
            }else{
                if(prev>biggest) biggest=prev;
                prev = now;
            }
        }
        if(prev>biggest) biggest=prev;
        if(biggest>k) return 1;//error, Bad!
        return 0;
    }*/
}
