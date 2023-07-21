//應該以全部的質數來分析，也就是先建出 prime[i], 然後避開 前3個(2,3,5) 之後全殺
//但是可惜，篩子法會超時，沒有必要用它。
//看了Editorial解答後，發現更簡單的方法，2，3，5 依序乘出最小的答案
bool buildTable = false; //因為C版的global變數會共用，能讓buildTable只做一次
long long int ugly235[1700], N=1; //ugly235[0]不使用哦！
int min(int a, int b, int c){
    if(a<=b && a<=c) return a;
    else if(b<=a && b<=c) return b;
    else return c;
}
int nthUglyNumber(int n){
    if(!buildTable){ //只算1次，是很帥的加速法
        buildTable = true;
        ugly235[1] = 1; //ugly235[0]不使用哦！
        int i2=1, i3=1, i5=1;
        //ugly235[i2]*2 vs. ugly235[i3]*3 vs. ugly235[i5]*5
        for(int i=2; i<=1690; i++){
            int a = ugly235[i2]*2, b = ugly235[i3]*3, c = ugly235[i5]*5;
            ugly235[i] = min(a, b, c);
            if(ugly235[i]==ugly235[i2]*2) i2++;
            if(ugly235[i]==ugly235[i3]*3) i3++;
            if(ugly235[i]==ugly235[i5]*5) i5++;
            //printf("%d ", ugly235[i] );
        }
    }
    return ugly235[n];
}
/*
bool buildTable = false;
int ugly235[1700], N=0;
int prime[6000], P=0; //計算6000以下的質數個數，本來是開20000
int nthUglyNumber(int n){
    //看到題目，讓我想到「質數篩子法」，只是不知道陣列要開多大
    //因為 n <=1690, 而2的倍數一定是，因此table只需要開 ...no
    //經過測試 ugly[1690]是5555，所以其實開6000就夠了
    if(!buildTable){
        buildTable = true;

        int killed[6000]={};
        for(int i=2; i<6000; i++){
            if(killed[i]==0){
                prime[P++] = i;
                for(int k=i; k<6000; k+=i) killed[k] = 1;
            }
        }
        printf("prime N:%d\n", P); //原來20000以下的質數有2262個
        int uglyOthers[6000]={}; //ugly235 是題目想要的，
        //所以uglyOthers[i]==1表示其他的
        for(int p=3; p<P; p++){ //2萬以下有2262個質數 or 6千以下有783個質數
            for(int k=prime[p]; k<4000; k+=prime[p]) uglyOthers[k] = 1;
        }
        for(int i=0; i<6000 && N<1700; i++){
            if(uglyOthers[i]==0) ugly235[N++]=i;
        }//20000個數字，只有5555個 ugly235
        printf("N:%d ugly235[1690]:%d\n", N, ugly235[1690]);
    }
    return ugly235[n];
}
//case: 1690 對應的答案是 2123366400 所以陣列顯然要開最大，memory不夠，也會超時
*/
