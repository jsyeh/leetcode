class Solution {
    public long countPairs(int n, int[][] edges) {
        //先分群，統計出字數，再依照「排列組合」來乘出答案
        //ex. 1 2 4 則答案是 1*2 + 1*4 + 2*4
        //但是n=100000 會造成超時
        boolean [] visited = new boolean[n];
        int [] label = new int[n];
        for(int i=0; i<n; i++){
            label[i] = i;
        }

        //ArrayList<Set<Integer>> sets = new ArrayList<Set<Integer>>();
        ArrayList<Integer> groups = new ArrayList<Integer>();
        ArrayList<Integer> [] lists = new ArrayList[n];
        for(int i=0; i<n; i++){
            lists[i] = new ArrayList<Integer>();
        }

        for(int i=0; i<edges.length; i++){
            int a = edges[i][0], b = edges[i][1];
            lists[a].add(b);
            lists[b].add(a);
        }

        for(int i=0; i<n; i++){
            if(!visited[i]){
                LinkedList<Integer> queue = new LinkedList<Integer>();
                //Set<Integer> set = new HashSet<Integer>();
                //sets.add(set);

                //set.add(i);
                int groupN = 1;

                queue.push(i);
                visited[i]=true;

                while(queue.size()>0){
                    int next = queue.pop();
                    ArrayList<Integer> list = lists[next];
                    for(int k=0; k<list.size(); k++) {
                        int one = list.get(k);
                        if(!visited[one]){
                            label[one]=i;

                            groupN++;
                            //set.add(one);
                            queue.push(one);
                            visited[one]=true;
                        }
                    }
                }
                groups.add(groupN);
            }
        }
        //if(n==100000) return 0;
        //沒想到n=100000時，下面的迴圈會超時，因為加了40億個1
        long ans=0;
        //想到一個解法，是統計不同次數會有幾個，使用map
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        //map key:大小 val:次數 ex. 1 1 1 1 2 會有 1:4 2:1
        for(int i=0; i<groups.size(); i++){
            int N = groups.get(i);
            if(!map.containsKey(N)){
                map.put(N, 1);
            }else{
                map.put(N, map.get(N)+1);
            }
        }
        long [] size = new long[map.size()];
        long [] repeat = new long[map.size()];
        int setN=0;
        for(Integer x : map.keySet()){
            size[setN] = x;
            repeat[setN] = map.get(x);
            setN++;
        }

        for(int i=0; i<setN; i++){
            ans += size[i]*size[i]*repeat[i]*(repeat[i]-1)/2;
            for(int j=i+1; j<setN; j++){
                ans += size[i]*repeat[i]*size[j]*repeat[j];
            }
        }
/*        for(int i=0; i<groups.size(); i++){
            for(int j=i+1; j<groups.size(); j++){
                ans += groups.get(i) * groups.get(j);
            }
        }*/
        return ans;
    }
}//case3: 100000 []
