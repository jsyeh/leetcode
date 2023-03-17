class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        int ans=0;
        for(int i=left; i<=right; i++){
            int c1 = words[i].charAt(0), c2 = words[i].charAt(words[i].length()-1);
            if((c1=='a'||c1=='e'||c1=='i'||c1=='o'||c1=='u')&&(c2=='a'||c2=='e'||c2=='i'||c2=='o'||c2=='u')) ans++;
        }
        return ans;
    }
}
