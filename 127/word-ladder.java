class Solution {
    HashMap<String,ArrayList<Integer>> map = new HashMap<>();
    HashMap<String,Integer> id = new HashMap<>();
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        wordList.add(beginWord);
        for(int i=0; i<wordList.size(); i++){ 
            String word = wordList.get(i);
            map.put(word, new ArrayList<Integer>()); //map to neighbors
            id.put(word, i);//map to word id
//System.out.println(word + " " + i);
        }
        if(!map.containsKey(beginWord)){
            map.put(beginWord, new ArrayList<Integer>() );
            id.put(beginWord, wordList.size());
        }

        //這題的加速部分，在建 neighbors關係，也就是用 HashMap 來加速確認相鄰關係
        for(int i=0; i<wordList.size(); i++){
            String word = wordList.get(i);
//System.out.println("word:" + word);
            byte [] s = word.getBytes();
            for(int k=0; k<s.length; k++){//挑一個字母要換
                byte orig = s[k];
                for(byte a='a'; a<='z'; a++){//
                    if(a==orig) continue;//試26個字母，但不能完全相同，也就是避開orig
                    s[k] = a;
                    String temp = new String(s);

                    //避開一開始的值：其他字不要指回beginWord

                    if(map.containsKey(temp)){ //找到相鄰字（只差1字母）
                        ArrayList<Integer> list = map.get(word);
                        list.add(id.get(temp));//word to temp
//System.out.println(". temp:" + temp + id.get(temp) + " to word " + id.get(word));
                        ArrayList<Integer> list2 = map.get(temp);
                        list2.add(id.get(word));//temp to word
//System.out.println(". word:" + word + id.get(word) + " to temp " + id.get(temp));
                    }
                }
                s[k] = orig;
            }
        }//以上迴圈可建出 neighbors 的關係
//System.out.println("hello");

        Queue<String> Q = new LinkedList<>();
        HashMap<String,Integer> visited = new HashMap<>();
        Q.offer(beginWord);
        visited.put(beginWord, 1);

        while(Q.size()>0){
//System.out.println("inside while");
            String word = Q.poll();
            int dist = visited.get(word);
            if(word.compareTo(endWord)==0) return dist;

            for(Integer i : map.get(word)){
//System.out.println(i);
//System.out.println(wordList.get(i));
                String next = wordList.get(i);
                if(!visited.containsKey(next)){
                    Q.offer(next);
                    visited.put(next, dist+1);
                }
            }
        }
        return 0;
    }
}
