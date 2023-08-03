class Solution {
    HashMap<String,Integer> chainLen = new HashMap<>();
    //chainLen, 裡面會存「某個字」往簡單走，最長可以走幾步 chainLen.get(word)

    public int longestStrChain(String[] words) {
        int ans = 1; //總會有第一代嘛
        Arrays.sort(words, (a,b)->a.length()-b.length());
        //字會從簡單到複雜。建立「chainLen」也是簡單到複雜
        for(String word : words) { 
            //現在處理某個字word，逐一去除裡面的單一字母，變shorter
            //看它有沒有 chainLen 的值，存最大的值+1
            int len = 1; //自己本身，可當第一代（祖傳三代名店，目前第一代）
            for(int i=0; i<word.length(); i++) {
                String shorter = word.substring(0,i) + word.substring(i+1);
                //shorter 是 word 可能的下一代。要認定「以前」有沒有出現過
                if(chainLen.containsKey(shorter)){ //以前有出現過的話
                    int len2 = chainLen.get(shorter)+1; //它的值拿來用
                    if(len2>len) len = len2; //更長，太好了，更新
                }
            }
            chainLen.put(word, len); //存最長的值
            if(len>ans) ans = len; //如果答案更好，就更新
        }
        return ans;
    }
}
