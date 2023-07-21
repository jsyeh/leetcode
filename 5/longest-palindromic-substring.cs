public class Solution {
    public string LongestPalindrome(string s) {
        //我決定用最早的笨方法，暴力去巡，因字串長度只有1000
        int maxI = 0, maxLen = 0, N = s.Length;
        for(int i=0; i<N; i++){ //中間的點
            //如果是奇數的迴文的話
            int len1=1, maxK=0;
            for(int k=1; i-k>=0 && i+k<N; k++){
                if(s[i-k] != s[i+k]) break;
                else {
                    maxK = k; //更好的k
                    len1 = k*2+1; //更長的 len1
                }
            }
            if(len1>maxLen){
                maxLen = len1; //迴文的長度
                maxI = i - maxK; //迴文的開始位置
            }
            //如果是偶數的迴文的話
            int len2=0;
            for(int k=1; i-k>=0 && i+k-1<N; k++){
                if(s[i-k] != s[i+k-1]) break;
                else {
                    maxK = k;
                    len2 = k*2;
                }
            }
            if(len2>maxLen){
                maxLen = len2;
                maxI = i - maxK;
            }
        }
        return s.Substring(maxI, maxLen);
    /*
        //以下想法是失敗的，因為 aacabdkacaa 會找到不是迴文的 aaca
        //想法：Palindrome 可以把 s 倒過來 (或是利用 index 修正的技巧)
        // table[i][j] 表示 包含 s[i] 及 t[j] 的最長 Palindrome
        // 這樣要找答案時，便找到table最大值時，再往前數幾格，便是答案
        int N = s.Length;
        char[] t = new char[N];
        for(int i=0; i<N; i++){
            t[i] = s[N-1-i];
        }

        int[,] table = new int[N+1, N+1];
        for(int i=0; i<=N; i++) {
            table[i,0] = 0;
            table[0,i] = 0;
        }
        int maxLen = 0;
        int maxII = 0, maxJJ = 0; //maxII, maxJJ 對應最大的 maxLen發生的地方
        for(int i=1; i<=N; i++) {
            for(int j=1; j<=N; j++) {
                if(s[i-1]==t[j-1]) table[i,j] = table[i-1,j-1] + 1;
                else{
                    table[i,j] = 0;
                }
                if(table[i,j]>maxLen){
                    maxLen = table[i,j];
                    maxII = i;
                    maxJJ = j;
                }
Console.Write(table[i,j] + " ");
            }
Console.WriteLine();
        }
Console.WriteLine(maxLen);
        char[] ans = new char[maxLen];
        for(int i=0; i<maxLen; i++){
            ans[i] = s[maxII-maxLen+i];
        }
        return new string(ans);
        */
    }
}
//case 134/141: "aacabdkacaa"
//我原本的想法有錯，是直接把字串倒過來，但
