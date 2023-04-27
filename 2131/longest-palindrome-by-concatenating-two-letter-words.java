class Solution {
    HashMap<String,LinkedList<Integer>> map = new HashMap<String,LinkedList<Integer>>();
    //map會將字 對應 出現的 index 以便之後標示 used[index]=true
    public int longestPalindrome(String[] words) {
        int N = words.length;
        boolean [] used = new boolean[N];
        boolean [] dd = new boolean[N];//疊疊字 duplicate double character

        int ans=0;
        for(int i=0; i<N; i++){
            if(words[i].charAt(0)==words[i].charAt(1)) dd[i] = true;

            String rev = words[i].charAt(1) + "" + words[i].charAt(0); //反向字
            if(map.containsKey(rev) && map.get(rev).size()>0) { //太好了, 有向反向字可對消
                LinkedList<Integer> list = map.get(rev);
                int index = list.pop(); //消掉1組字
                used[index] = true;
                used[i] = true;
                ans += 4; //因為有對應, 所以 ans 有2組字可組合, ans+=4
            } else { //沒有反向字可對消, 就把 words[i] 加入 map 中
                if(map.containsKey(words[i])) { //之前有加過
                    LinkedList<Integer> list = map.get(words[i]);
                    list.push(i);
                } else {
                    LinkedList<Integer> list = new LinkedList<Integer>();
                    list.push(i);
                    map.put(words[i], list);
                }
            }
        }

        for(int i=0; i<N; i++){
            if(dd[i]==true && used[i]==false){//又有找到1組沒用過的疊字
                ans+=2;
                break;
            }
        }
        return ans;
    }
}//case 7/120: ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
//字用完後, map裡面怎麼辦
//case 108/120: ["bb","bb"] 要記得 2個都要 used[i]=true;
