int minCost(int** costs, int costsSize, int* costsColSize) {
    //costs[h][c] 對應 house h 漆成 color c 對應的 cost
    int arr[2][3]; // 用來放 prevCost 及 nextCost
    int * prevCost = arr[0], * nextCost = arr[1];
    // prevCost[i] 對應「最後一間漆 color i 」對應的min cost
    for(int c=0; c<3; c++) nextCost[c] = costs[0][c];

    for(int h=1; h<costsSize; h++){ //接著逐房更新
        //每次開始前，要將 prevCost 及 nextCost 做交換
        int * temp = prevCost;
        prevCost = nextCost;
        nextCost = temp;
        for(int c=0; c<3; c++){ //現在要漆 color c
            int prevMin = INT_MAX;
            for(int c2=0; c2<3; c2++){ //之前漆 c2
                if(c==c2) continue; // 色彩不能重覆，避開
                if(prevCost[c2]<prevMin) prevMin = prevCost[c2];
            }
            nextCost[c] = prevMin + costs[h][c];
        }
    }
    int ans = nextCost[0]; //最後3個cost看哪個最小
    if(nextCost[1]<ans) ans = nextCost[1];
    if(nextCost[2]<ans) ans = nextCost[2];
    return ans;
}
