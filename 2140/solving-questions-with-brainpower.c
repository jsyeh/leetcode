long long mostPoints(int** questions, int questionsSize, int* questionsColSize){
    int N = questionsSize;
    long long table[N+1];//table[i] 表示「如果question i 有回答,最多得幾分」
    //這也代表, 前面要查很多次,會浪費太多時間。
    //所以Editoral 裡介紹的方法, 是倒過來想(從最後面往前面想)
    //table[i] 的最佳值是什麼, 有兩種可能: (1) 如果要用第i題,就是 value[i] + table[i+brainpower[i]]
    //也就是了第i題, 則後面很多題都不能做, 要休息, 直到後面第 i+brainpower[i]題, 所以要加上它的值
    //(2) 如果不用第i題, 就看 table[i+1] 那格的值
    //去找 (1) (2) 的最大值
    //最後, table[0] 是答案

    table[N] = 0;
    table[N-1] = questions[N-1][0];
    for(int i=N-1; i>=0; i--){
        int points = questions[i][0];
        int delay = questions[i][1];//要花一些腦力、一段間
        //table[i] = max(table[i+1], points+table[i+delay+1]);
        //本來應該照上面的寫, 不過因為 i+delay+1可能超過陣列大小, 所以要改寫
        table[i] = points;
        if(i+delay+1<N) table[i] += table[i+delay+1];
        if(table[i+1]>table[i]) table[i] = table[i+1];
    }
    return table[0];
}
