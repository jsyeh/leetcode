class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int N = triangle.size();
        int[] table = new int[N];
        List<Integer> list0 = triangle.get(N-1);
        for(int k=0; k<list0.size(); k++){
            table[k] = list0.get(k);
        }
        for(int i=N-2; i>=0; i--) {
            List<Integer> list = triangle.get(i);
            for(int k=0; k<list.size(); k++) {
                table[k] = min(table[k],table[k+1]) + list.get(k);
            }
        }
        return table[0];
    }
    int min(int a, int b) {
        if(a<b) return a;
        else return b;
    }
}
