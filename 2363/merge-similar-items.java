class Solution {
    public List<List<Integer>> mergeSimilarItems(int[][] items1, int[][] items2) {
        List<List<Integer>> ans = new ArrayList<>();  // 用來放答案
        Arrays.sort(items1, (a,b)->a[0]-b[0]);  // 先個別排序
        Arrays.sort(items2, (a,b)->a[0]-b[0]);  // 先個別排序
        for(int i=0, j=0; i<items1.length || j<items2.length;  ) {
            if(i<items1.length && j<items2.length) {  // 兩個 index 都還沒走到盡頭
                if(items1[i][0]==items2[j][0]) { // 相同value就合併weight
                    ans.add(Arrays.asList(items1[i][0], items1[i][1]+items2[j][1]));
                    i++;
                    j++;
                }else if(items1[i][0]<items2[j][0]) { // 把小的 value 拿去用
                    ans.add(Arrays.asList(items1[i][0], items1[i][1]));
                    i++;
                }else { // 把小的 value 拿去用
                    ans.add(Arrays.asList(items2[j][0], items2[j][1]));
                    j++;
                }
            }else if(i<items1.length) { //只剩i還沒走到盡頭
                ans.add(Arrays.asList(items1[i][0], items1[i][1]));
                i++;
            }else { //只剩j還沒走到盡頭
                    ans.add(Arrays.asList(items2[j][0], items2[j][1]));
                    j++;
            }
        }
        return ans;
    }
}
