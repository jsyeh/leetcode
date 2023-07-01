int distributeCookies(int* cookies, int cookiesSize, int k){
    int N = cookiesSize; //N最大是8
    int table[k+1][256];
    //有2^8＝256種可能的分配法, table[p][256] 表示p個人分8包糖，全部排列組合，最小的unfair值

    //下面建立 sum[mask] 會對照「如果收到包，約共有多少糖果」
    int sum[256];
    for(int mask=0; mask<(1<<N); mask++){ //ex. N為4時: 0000 ~ 1111
        int total = 0;
        for(int i=0; i<N; i++){
            if((mask & (1<<i)) > 0) total += cookies[i];
            //如果 mask 對應第i bit有這包，那就加上 cookies[i] 這包的糖果量
        }
        sum[mask] = total;
        table[0][mask] = INT_MAX; //最一開始的值設INT_MAX，以便隨時換掉
    }

    table[0][0] = 0; //0個人分，全部都沒有拿，拿最多的人是0顆糖
    for(int p=1; p<=k; p++){
        for(int mask=0; mask<(1<<N); mask++){ //去試各種排列組合
            table[p][mask] = INT_MAX;//先設最大值
            for(int submask=mask; submask>0; submask = (submask-1)&mask){
            //技巧來自https://leetcode.com/problems/fair-distribution-of-cookies/solutions/2141573/dp-submask-enumeration-most-optimal-solution-100-faster-c/
            //它的意思是，mask 的子集合，可用 (submask-1)&mask 把全部子集合的排列組合也都試過一次
                int unfair = table[p-1][mask^submask];
                //如果人比較少，且一樣的submask 的分法，最好的值
                //前面p-1個人是分 mask - submask 的包
                //而第p個人是分 submask 的包
                //這時候，最不公平/分最多的那個人，是分多少個糖果？
                if(sum[submask]>unfair) unfair = sum[submask];

                //table[p][mask] 裡面存 p 人時，只有 mask 對應糖果能分配時，最好的分配的答案（也就是分最多的那個人要最小的值是多少）
                if(unfair < table[p][mask]) table[p][mask] = unfair;
            }
        }
    }
    return table[k][(1<<N)-1];//k個人，全部的糖都分下去時，unfair最小的值

    return 0;
}
