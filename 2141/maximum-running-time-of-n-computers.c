//Editorial 介紹了兩種演算法，分別是有技巧的greedy演算法，及binary search法
//我先照著第1種方法來實作
int comp(const void *p1, const void *p2){
    return *(int*)p1 - *(int*)p2;
}
long long maxRunTime(int n, int* batteries, int batteriesSize){
    qsort(batteries, batteriesSize, sizeof(int), comp);
    long long live[n];
    for(int i=0; i<n; i++){
        live[i] = batteries[batteriesSize-n+i];
    }//把時間最長的batteries 設定給 n 台電腦，便能先知道這幾台電腦目前的使用時間
    //ex. 1 2 3 4 5 給n=3台電腦，便將 live[i] 設成 3 4 5

    long long extra = 0;
    for(int i=0; i<batteriesSize-n; i++){
        extra += batteries[i]; //剩下的電池，都可以拿來支援用，統籌管理
    }

    long long ans = live[0]; //拿來使用的前n大電池，相對最短的那個瓶頸
    for(int i=0; i<n-1; i++){ //逐一去補短缺的電力，最長電力的那個先不用去補它
        int diff = live[i+1] - live[i]; //相對短缺的電力
        if(extra>=diff*(i+1)){ //足夠填補電力缺口時
            extra -= diff*(i+1); //電力讓live[i]之前都補齊
        }else{
            //如果補不齊，應該要「能補多少，就補多少」不能直接return瓶頸
            //錯 return live[i];//若不夠補，這時候的瓶頸就是答案
            return live[i] + extra/(i+1);
        }
    }
    //程式能走到這裡，表示瓶頸都補完了，大家的電力都用到最大的 live[n-1]那根
    return live[n-1] + (extra/n); //所以剩下的extra電力，便能拿來平均分配
}
//這個greedy演算法蠻巧妙的，試過一些測試資料，都沒有問題。
//case 38/52: 3 [10,10,3,5] 取出 [5,10,10],接著 3要補到5
