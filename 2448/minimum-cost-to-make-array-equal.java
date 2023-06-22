class Solution {
    public long minCost(int[] nums, int[] cost) {
        int n = nums.length;
        //sorting
        int [][] a = new int[n][2];
        for(int i=0; i<n; i++){
            a[i][0] = nums[i];
            a[i][1] = cost[i];
        }
        Arrays.sort(a, (i,j)->i[0]-j[0]);

        //prefix sum of cost
        long [] prefixSum = new long[n];
        long [] suffixSum = new long[n];
        prefixSum[0] = a[0][1];
        for(int i=1; i<n; i++){
            prefixSum[i] = prefixSum[i-1] + a[i][1];
        }
        suffixSum[n-1] = a[n-1][1];
        for(int i=n-2; i>=0; i--){
            suffixSum[i] = suffixSum[i+1] + a[i][1];
        }

        //如果答案是. a[0][0] 的話，其他數字要配合它嘛
        long total_cost = 0, LLL=1;
        for(int i=1; i<n; i++){//固定 a[0][0], 其他全加一次
            total_cost += LLL * a[i][1] * (a[i][0]-a[0][0]); //乘上 LLL 就變 long 才不會overflow
        }
//System.out.println("total_cost: " + total_cost);

        long ans = total_cost;
        for(int k=1; k<n; k++){ //想固定 a[k][0]
            long dist = a[k][0] - a[k-1][0]; //提昇多少值
            total_cost += prefixSum[k-1]*dist; //加上左邊的prefix
            total_cost -= suffixSum[k]*dist; //減掉右邊的suffix
            if(total_cost<ans) ans = total_cost;
//System.out.println("total_cost: " + total_cost);
        }

        return ans;
    }
}
//case 11/48: [735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518]
//[724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]
//它的答案是 1907611126748 但我的答案是 -2773903225892 可見我的程式有 overflow
