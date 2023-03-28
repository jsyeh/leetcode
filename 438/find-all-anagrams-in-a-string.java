class Solution {
    int [] H1;
    int [] H2;
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<Integer>();
        int N1 = s.length(), N2 = p.length();
        if(N1<N2) return ans;

        H1 = new int[26];
        H2 = new int[26];

        for(int i=0; i<N2; i++){//先前面n2位，讓長度與p相同
            H1[s.charAt(i)-'a']++;
        }
        for(int i=0; i<N2; i++){
            H2[p.charAt(i)-'a']++;
        }
        if(check()) ans.add(0);

        for(int i=1; i<=N1-N2; i++){
            H1[s.charAt(i+N2-1)-'a']++;
            H1[s.charAt(i-1)-'a']--;
            if(check()) ans.add(i);
        }
        return ans;
    }
    boolean check(){
        for(int i=0; i<26; i++){
            if(H1[i]!=H2[i]) return false;
        }
        return true;
    }
}
