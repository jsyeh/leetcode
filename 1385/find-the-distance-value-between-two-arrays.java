class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        int ans=0;
        for(int i=0; i<arr1.length; i++){
            int bad=0;
            for(int j=0; j<arr2.length; j++){
                int diff = (arr1[i]-arr2[j]);
                if(diff<0) diff = -diff;
                if(diff<=d) bad=1;
            }
            if(bad==0) ans++;
        }
        return ans;
    }
}
