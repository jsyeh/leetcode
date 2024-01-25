// 使用 DP 來解決 LCS 的問題
public class Solution {
    public int LongestCommonSubsequence(string text1, string text2) {
        int N1 = text1.Length, N2 = text2.Length;
        int [,] table= new int[N1+1,N2+1];
        //table[i][j] 比對到 text1[i] text2[j] 對應的 LCS 長度
        for(int i=0; i<N1; i++){
            for(int j=0; j<N2; j++){
                // 如果對應的字元相同，就升級+1
                if(text1[i]==text2[j]) table[i+1,j+1] = table[i,j] + 1;
                // 下面分別看隔壁鄰居
                table[i+1,j+1] = Math.Max(table[i+1,j+1], table[i+1,j]);
                table[i+1,j+1] = Math.Max(table[i+1,j+1], table[i,j+1]);
            }
        }
        return table[N1,N2]; // 最後比完的答案
    }
}
