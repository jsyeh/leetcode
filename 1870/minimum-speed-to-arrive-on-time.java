class Solution {
    public int minSpeedOnTime(int[] dist, double hour) {
        //Arrays.sort(dist);//讓最小的在 dist[0] 不能排序，因題目要照順序搭車

        int left=1, right=Integer.MAX_VALUE-1;

        int good=0;
        while(left<right){
            int mid=(int)((left+(double)right)/2);//小心會overflow
            double sum=0;
            for(int i=0; i<dist.length-1; i++){
                sum+= Math.ceil(dist[i]/(double)mid);
            }
            sum+=dist[dist.length-1]/(double)mid;

            System.out.print(mid + " " + sum);
            if(sum<=hour){//good,可以再慢一點
                right=mid;
                good++;
            }else{//糟糕，不行，要再快一點
                left = mid+1;
            }
            System.out.println(" "+left+" "+right);
        }
        if(good==0) return -1;
        else return left;
    }
}//case 56/65: [1,1,100000] 2.01 它的答案是 10_000_000 但我算出 10_000_0 ，原來最後一趟才另外處理
