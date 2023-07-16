//這題  req_skills.length <= 16 看起來就像 bit masking 的題型
//參考 lee215 的解法 https://leetcode.com/problems/smallest-sufficient-team/solutions/334572/java-c-python-dp-solution/
class Solution {
    //HashMap<String,Integer> skill_index = new HashMap<>();
    HashMap<String,Integer> skill_mask = new HashMap<>();
    public int[] smallestSufficientTeam(String[] req_skills, List<List<String>> people) {

        int N = req_skills.length; //用來建表格： skill Number
        int P = people.size(); //有幾個人可以挑選： People number
        int maskN = 1<<N; //mask number
        for(int i=0; i<req_skills.length; i++){
            //skill_index.put(req_skills[i], i); //String 對照到 index 
            skill_mask.put(req_skills[i], 1<<i); //String 對照到 mask
        }
        ArrayList<Integer> [] table = new ArrayList[maskN];//超大對照表
        // table[mask].get(i) 表示 mask 的技能組合，如果考慮前i個人的話，挑誰？
        table[0] = new ArrayList<>(); //沒有任何skill mask bit的話，其實都不用挑
        for(int i=0; i<P; i++){ //現在考慮第 i 個人
            int i_skill_mask = 0; //第i個人，對應的mask
            for(String skill : people.get(i)){
                i_skill_mask |= skill_mask.get(skill);
            }
            //暴力排列組合，看所有的 mask 在有了 i_skill_mask 後，有什麼改變
            for(int mask=0; mask<maskN; mask++){
                if(table[mask] == null) continue;
                //若「舊的mask」都沒有運作過，那就不用更新「新的mask」
                //還好在迴圈前 table[0] = new ArrayList<>() 已建最基礎的空白的答案

                int newMask = mask | i_skill_mask; //有了i-th人之後，新的mask
                if(table[newMask] == null){ //創造出從來沒出現過的 skill mask set
                    //第一次進來的話，就照這種作法，從 mask + i
                    table[newMask] = new ArrayList<>(table[mask]);
                    //從舊的mask 複製出新的 mask，並補齊新增加的內容
                    table[newMask].add(i); //新的mask可由i來協助做出來
                }else if(table[mask].size()+1 < table[newMask].size()){
                    table[newMask] = new ArrayList<>(table[mask]);
                    table[newMask].add(i);
                } //精華重點：現在這種挑法(mask+第i人)，比舊的table[newMask]挑法更好
            }
        }

        //把答案從 ArrayList<Integer> 轉換成 int[]
        ArrayList<Integer> result = table[maskN-1];
        int [] ans = new int[result.size()];
        for(int i=0; i<result.size(); i++){
            ans[i] = result.get(i);
        }
        return ans;
    }
}
