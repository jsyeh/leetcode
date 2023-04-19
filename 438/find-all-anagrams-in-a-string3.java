class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        HashMap<Character,Integer> map1 = new HashMap<Character,Integer>();
        HashMap<Character,Integer> map2 = new HashMap<Character,Integer>();
        for(int i=0; i<p.length(); i++){
            char c = p.charAt(i);
            if(map2.containsKey(c)){
                map2.put(c, map2.get(c)+1);
            }else map2.put(p.charAt(i), 1);
        }
        List<Integer> ans = new ArrayList<Integer>();
        int len2 = p.length();
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(map1.containsKey(c)){
                map1.put(c, map1.get(c)+1);
            }else map1.put(c, 1);

            if(map1.equals(map2)) ans.add(i-len2+1);

            if(i>=len2-1){
                char c2 = s.charAt(i-len2+1);
                if(map1.get(c2)>1) map1.put(c2, map1.get(c2)-1);
                else map1.remove(c2);
            }
        }
        return ans;
    }
}
