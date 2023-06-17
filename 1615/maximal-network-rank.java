class Solution {
    HashSet<Integer> set = new HashSet<>();
    public int maximalNetworkRank(int n, int[][] roads) {
        //想到可用 HashMap來查「某兩city」間有沒有相連
        //所以就暴力法：先建出全部的city的相關數目，再查HashMap看是否相連
        int []neighbor = new int[n];
        for(int i=0; i<roads.length; i++){
            int a = roads[i][0], b = roads[i][1];
            neighbor[a]++;
            neighbor[b]++;
            set.add(a*100+b);//因<100,可這樣建出整數
            set.add(b*100+a);//兩個都建
        }
        int ans = 0;
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                int temp = neighbor[i]+neighbor[j];
                if(set.contains(i*100+j)){
                    //隨便試一種就可
//System.out.print(".");
                    temp--;
                }
                if(temp>ans) ans = temp;
            }
        }
        return ans;
    }
}
