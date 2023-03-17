class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        int [] soldiers = new int[mat.length];
        int [] id = new int[mat.length];
        for(int i=0; i<mat.length; i++){
            id[i] = i;
        }
        for(int i=0; i<mat.length; i++){
            soldiers[i]=0;
            for(int j=0; j<mat[i].length; j++){
                if(mat[i][j]==1) soldiers[i]++;
            }
        }
        for(int i=0; i<k; i++){
            for(int j=mat.length-2; j>=0; j--){
                if(soldiers[j]>soldiers[j+1]){
                    int temp = soldiers[j];
                    soldiers[j] = soldiers[j+1];
                    soldiers[j+1] = temp;
                    temp = id[j];
                    id[j] = id[j+1];
                    id[j+1] = temp;
                }
            }
        }
        int [] ans = new int[k];
        for(int i=0; i<k; i++){
            ans[i] = id[i];
        }
        return ans;
    }
}
