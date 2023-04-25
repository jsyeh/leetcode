class Solution {
    HashMap<String,Integer> map = new HashMap<String,Integer>();
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> ans = new ArrayList<String>();

        for(int i=0; i<s.length()-10+1; i++){
            String now = s.substring(i, i+10);
            if(map.containsKey(now)){
                if(map.get(now)==1){
                    ans.add(now);
                }
                map.put(now, map.get(now)+1);
            }else map.put(now, 1);
        }
        return ans;
    }
}//case 25/31: "AAAAAAAAAAA"
