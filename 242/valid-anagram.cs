public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length!=t.Length) return false; //長度不同，就失敗

        int [] H1 = new int[26]; //陣列，統計字母次數
        int [] H2 = new int[26];
        foreach(char c in s){ //統計第1個字串
            H1[c-'a']++;
        }
        foreach(char c in t){ //統計第2個字串
            H2[c-'a']++;
        }
        for(int i=0; i<26; i++){ //26個字母逐個比對
            if(H1[i]!=H2[i]) return false;
        }
        return true; //都沒失敗，就是成功了
    }
}
