bool d[100][100]; // if(d[i][j]) 表示 bombi 可炸到 bombj
bool visited[100] = {}; //不知道為什麼陣列當參數傳給函式的話會爆掉。或許要傳指標才行

bool effect(long long x, long long y, long long r, long long x2, long long y2){
    if((x-x2)*(x-x2)+(y-y2)*(y-y2)<=r*r) return true;
    else return false;
}

void visiting(int k, int N, int * ans){
    (*ans)++;
    visited[k] = 1;
    for(int i=0; i<N; i++){
        if(visited[i]==0 && d[k][i]){
            visiting(i, N, ans);
        }
    }
}

int maximumDetonation(int** bombs, int bombsSize, int* bombsColSize){
    //Idea; 有100個bomb,所以用兩層迴圈,建出 int d[100][100]; 其中 d[i][j] 表示 i 可以炸到j
    //然後再用暴力法,去試 100個bomb 各自可以引爆幾個bomb
    for(int i=0; i<bombsSize; i++){
        for(int j=0; j<bombsSize; j++){
            //想確認 bombs[i] 是否會引爆 bomb[j]
            int x = bombs[i][0], y = bombs[i][1], r = bombs[i][2];
            int x2 = bombs[j][0], y2 = bombs[j][1];
            if(i==j) d[i][j] = false; //為了簡化程式,自己不炸自己
            else if( effect(x,y,r,x2,y2) ) d[i][j] = true;
            else d[i][j] = false;
        }
    }
    int ans = 1;
    for(int i=0; i<bombsSize; i++){
        int now = 0;
        for(int k=0; k<bombsSize; k++) visited[k] = false;
        visiting(i, bombsSize, &now);
        if(now>ans) ans = now;
    }
    return ans;
}
//case 12/160: [[1,1,100000],[100000,100000,1]]
//case 74/160: [[858,869,75],[878,994,438],[166,911,336],[362,754,500],[55,656,400],[48,139,247],[758,655,241],[533,901,130],[474,624,400],[47,952,54],[551,501,334],[822,360,74],[674,881,271],[752,880,251],[381,669,158],[302,336,323],[779,790,98],[777,238,429],[569,817,213],[274,878,484],[380,639,196],[560,555,454],[25,175,185],[102,822,444],[600,434,282],[384,807,214],[62,288,159],[682,551,117],[312,934,279],[752,510,292],[666,739,467],[910,447,12],[869,821,47],[968,418,137],[592,535,319],[5,632,438],[229,686,471],[195,553,337],[792,127,331],[675,815,61],[929,100,14],[533,729,353],[284,700,158],[420,16,344],[767,66,110],[678,402,239],[608,974,451],[789,104,389],[764,516,336],[842,130,255],[54,705,229],[755,891,404],[891,563,93]]
