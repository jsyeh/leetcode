class Solution {
    Map<String, ArrayList<Integer>> map = new HashMap<String, ArrayList<Integer>>();
    public int shortestWordDistance(String[] wordsDict, String word1, String word2) {
        //問題在，竟然有相同的字。所以要分得出來
        for(int i=0; i<wordsDict.length; i++){
            String now = wordsDict[i];
            if(map.containsKey(now)){
                map.get(now).add(i);
            }else{
                ArrayList<Integer> temp = new ArrayList<Integer>();
                temp.add(i);
                map.put(now, temp);
            }
        }

        ArrayList<Integer> temp1 = map.get(word1);
        ArrayList<Integer> temp2 = map.get(word2);
        if(word1.equals(word2)){
            int ans = Integer.MAX_VALUE;
            for(int i=0; i<temp1.size()-1; i++){
                int dist = Math.abs(temp1.get(i) - temp1.get(i+1));
                if(dist<ans) ans = dist;
            }
            return ans;
        } else {
            int ans = Integer.MAX_VALUE;
            int i=0, j=0;
            while(i<temp1.size() && j<temp2.size()){
                int dist = Math.abs(temp1.get(i) - temp2.get(j));
                if(dist<ans) ans = dist;

                if(temp1.get(i)>temp2.get(j)){
                    j++;
                }else{
                    i++;
                }
            }
            return ans;
        }
        /*if(temp1==temp2){
            int ans = Integer.MAX_VALUE;
            for(int i=0; i<temp1.size(); i++){
                for(int j=i+1; j<temp1.size(); j++){
                    int now = Math.abs(temp1.get(i)-temp1.get(j));
                    if(now<ans) ans = now;
                }
            }
            return ans;
        }
        else{
            int ans = Integer.MAX_VALUE;
            for(int i=0; i<temp1.size(); i++){
                for(int j=0; j<temp2.size(); j++){
                    int now = Math.abs(temp1.get(i)-temp2.get(j));
                    if(now<ans) ans = now;
                }
            }
            return ans;
        }*/
    }
}//case3: ["a","c","a","a"] "a" "a"
//case4: 全部都相同，或是有50000 vs. 50000 要2層迴圈，有點麻煩。可以再用binarySearch()加快一些
