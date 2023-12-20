//在要找最便宜的2個巧克力, 所以在迴圈裡,找最小的2個數,再回傳「剩多少錢」
//錢不夠買時, 就不要買, 錢都留下來。
int buyChoco(int* prices, int pricesSize, int money){
    int min1 = 200, min2 = 200; //因 prices[i]<=100, 設200當成預設值
    for(int i=0; i<pricesSize; i++){
        if(prices[i]<min1){
            min2 = min1;
            min1 = prices[i];
        }else if(prices[i]<min2){
            min2 = prices[i];
        }
    }
    if(min1+min2 > money) return money; //錢不夠花,不要買
    else return money-min1-min2; //錢夠花, return 買剩的錢
}
