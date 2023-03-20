class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int N = flowerbed.length;
        int empty=1;
        int ans=0;
        for(int i=0; i<N; i++){
            if(flowerbed[i]==0) empty++;
            else{
                ans += table(empty);
                empty=0;
            }
            if(i==N-1 && flowerbed[i]==0) ans += table(empty+1);
        }
        if(ans>=n) return true;
        else return false;
    }
    int table(int empty) {
        if(empty<3) return 0;
        return (empty-1)/2; // 3:1 4:1 5:2 6:2 7:3
    }
} //case 3: [0,0,1,0,1] 最左邊有1個
//case 4: [0 0,1,0,0] 最右邊也可以有一個
