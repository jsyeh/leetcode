// 有幾位同學沒辦法吃午餐?
// 餐廳有提供 圓形0、方形1 的三明治, 同學也有各個自喜歡的三明治
// 規則: 學生排隊, 如果三明治喜歡就拿走, 不喜歡, 就再重新排隊
// 一直持續, 直到沒辦法再拿為止。
// 我本來想實作 circular array queue 但有點麻煩, 放棄。
// 改用 Solutions 裡 vashik 用的方法, 也就是「先數有幾個0、幾個1」
// 接下來, 以三明治的迴圈為主, 看有沒有人要拿。沒有人能再拿時, 答案就找到了。
int countStudents(int* students, int studentsSize, int* sandwiches, int sandwichesSize) {
    int zero=0, one=0;
    for(int i=0; i<studentsSize; i++){
        if(students[i]==0) zero++;
        else one++;
    }//統計完學生的喜好, 接下來以三明治的迴圈為主
    for(int i=0; i<sandwichesSize; i++){
        if(sandwiches[i]==0 && zero>0) zero--; // 目前是0 且有人喜歡0
        else if(sandwiches[i]==1 && one>0) one--; //目前是1 且有人喜歡1
        else break; // 都沒有人喜歡, 結束了
    }
    return one+zero; //剩下哪些學生還沒拿到三明治
}
