class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<Integer>();
        int N1=s.length(), N2=p.length();
        if(N1<N2) return ans;

        int [] H1 = new int[26];
        int [] H2 = new int[26];
        for(int i=0; i<p.length(); i++){
            H2[p.charAt(i)-'a']++;
        }

        for(int i=0; i<s.length(); i++){
            H1[s.charAt(i)-'a']++;
            if(i>=N2) H1[s.charAt(i-N2)-'a']--;
            if(checkAnagram(H1,H2)) ans.add(i-N2+1);
        }
        return ans;
    }
    boolean checkAnagram(int[] H1, int[] H2){
        for(int i=0; i<26; i++){
            if(H1[i]!=H2[i]) return false;
        }
        return true;
    }
}
