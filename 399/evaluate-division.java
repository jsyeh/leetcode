class NextNode {
    String s;
    double ratio;
    NextNode(String _s, double _r) {
        s = _s;
        ratio = _r;
    }
}
class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        //感覺上，像是graph的關係。有equations時，便代表有edge相連。query時，便是看怎麼相連的，找到路徑的edges便能算出答案。如果沒有edge相連，便回傳-1
        //一條equation代表不同的除法倍率，所以要產生2個edge
        //字串 to 下個字串 & 倍率
        HashMap<String,ArrayList<NextNode>> map = new HashMap<>();

        for(int eqID=0; eqID<equations.size(); eqID++){
            List<String> edge = equations.get(eqID);
            ArrayList<NextNode> list;
            if(map.containsKey(edge.get(0))) {
                list = map.get(edge.get(0));
            } else{
                list = new ArrayList<NextNode>();
            }
            list.add(new NextNode(edge.get(1), values[eqID]));
            map.put(edge.get(0), list);
            //從0對應到1是正向，直接使用value[eqID]

            if(map.containsKey(edge.get(1))) {
                list = map.get(edge.get(1));
            } else list = new ArrayList<NextNode>();
            list.add(new NextNode(edge.get(0), 1/values[eqID]));
            //從1對應到0是逆向，改使用 1/value[eqID]
            map.put(edge.get(1), list);
        }

        double[] ans = new double[queries.size()];
        int queryN = 0;
        for(List<String> query : queries) {
            HashSet<String> visited = new HashSet<>();
            if(!map.containsKey(query.get(0)) || !map.containsKey(query.get(1))) {
                ans[queryN++] = -1; //找不到字串，那就不可能有答案
            }else{
                ans[queryN++] = visiting(map, query.get(0), query.get(1), visited);
            }
        }
        return ans;
    }
    double visiting(HashMap<String,ArrayList<NextNode>> map, String from, String to, HashSet<String>visited) {

        if(from.equals(to)) return 1;
        if(visited.contains(from)) return -1;
        visited.add(from);

        ArrayList<NextNode> list = map.get(from);
        for(NextNode next : list){
            if(visited.contains(next.s)) continue;//走過就不進去
            double now = visiting(map, next.s, to, visited);
            if(now!=-1) return now * next.ratio;
        }
        return -1;
    }
}
