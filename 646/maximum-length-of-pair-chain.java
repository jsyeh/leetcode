// 我之前的解題策略是錯的，以為這題會用到 binary search
// 研究有些測資錯誤後，才發現根本不需要 binary search
// 只要從小到大，逐一查看能不能接起來（變長）即可
class Solution {
    public int findLongestChain(int[][] pairs) {
        int N = pairs.length;
        Arrays.sort(pairs, (a,b)->a[1]-b[1]);
        int ans = 0, end = -9999; //數字最小是-1000
        for(int[] pair : pairs) { //因pair[1] end數字從小到大
            if(pair[0]>end){ //所以能與 pair[0] 接起來的話，便能更新
                end = pair[1]; //接起來
                ans ++; //答案也更長了
            }
        }
        return ans;
    }
}
/*
class Solution {
    public int findLongestChain(int[][] pairs) {
        int N = pairs.length;
        // 先將 pairs 以結束時間排序，等下用binary search找誰能接起來
        Arrays.sort(pairs, (a,b)->(a[1]-b[1]!=0)?a[1]-b[1]:a[0]-b[0]);
        for(int i=0; i<N; i++){
            System.out.println(" " + pairs[i][0] + "," + pairs[i][1]);
        }

        int [] length = new int[N+1]; //想查 pairs[i] 之前已接多長
        int ans = 0;
        //都沒接時 length[0]長度0, length[i]表示pairs[i-1]能接的長度
        for(int i=1; i<N+1; i++) { //每次多考慮 pairs[i] 能接的狀況
            int left=0, right=i; // binary search
            while(left<right) {
                int mid = (left+right) / 2;
                if(pairs[mid][1] < pairs[i-1][0]) {
                    left = mid + 1; // pairs[mid] 結束時間夠接起來
                }else{ // pairs[mid] 結束時間不夠，要再早一些
                    right = mid;
                }
            } // 找到合適的位置時，便可接起來，長度 +1
            System.out.println("i:"+i+" left:"+left);
            length[i] = length[left] + 1;
            if(length[i]>ans) ans = length[i]; //更新答案
        }
        for(int i=0; i<=N; i++) System.out.print(" "+length[i]);
        return ans;
    }
}
*/
//case 89/206: [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]] 問題出在如果有兩個 [1,7] 和 [-4,7] 當初沒排序好，會用到差的那個
// 所以排序改成 Arrays.sort(pairs, (a,b)->(a[1]-b[1]!=0)?a[1]-b[1]:a[0]-b[0]);
//case 94/206: [[9,10],[9,10],[4,5],[-9,-3],[-9,1],[0,3],[6,10],[-5,-4],[-7,-6]]
// 0,1 2 1 1 3 4 5 5 5 但我算成了 0,1 2 1 1 2 3 4 4 4
