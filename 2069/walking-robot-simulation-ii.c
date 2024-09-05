// LeetCode 2069. Walking Robot Simulation II
// 原本的模擬 874. Walking Robot Simulation 進階，提供工具，讓別人呼叫
// 其實「只會繞四周走」答案是固定的，不用「一步步模擬」
typedef struct {
    int pos[2];
    int d;
} Robot;

int circle, robotI; // 圓周的格子數
Robot * obj; // pos[i] 是陣列，放圓周上每個點的Robot資訊
Robot* robotCreate(int width, int height) {
    circle = (width-1 + height-1) * 2;
    obj = (Robot*) malloc(sizeof(Robot)*circle);
    int i=0;
    for(int x=1; x<width; x++){ // 往東走
        obj[i].pos[0] = x;
        obj[i].pos[1] = 0;
        obj[i++].d = 0;
    }
    for(int y=1; y<height; y++){ //往北走
        obj[i].pos[0] = width-1;
        obj[i].pos[1] = y;
        obj[i++].d = 1;
    }
    for(int x=width-2; x>=0; x--){ //往西走
        obj[i].pos[0] = x;
        obj[i].pos[1] = height-1;
        obj[i++].d = 2;
    }
    for(int y=height-2; y>=0; y--){ //往南走
        obj[i].pos[0] = 0;
        obj[i].pos[1] = y;
        obj[i++].d = 3;
    }
    robotI = -1; // 一開始在起點，不是 pos[0] 哦！
    return obj;
}

void robotStep(Robot* obj, int num) {
    robotI = (robotI + num) % circle;
}

int* robotGetPos(Robot* obj, int* retSize) {
    *retSize = 2;
    if(robotI==-1) return obj[circle-1].pos; // 最一開始，是「起點」我放最後一格
    return obj[robotI].pos;
}

char directions[4][10] = {"East", "North", "West", "South"};
char* robotGetDir(Robot* obj) {
    if(robotI==-1) return directions[0]; // 最一開始，是「向東」
    return directions[obj[robotI].d];
}

void robotFree(Robot* obj) {
    free(obj);
}

/**
 * Your Robot struct will be instantiated and called as such:
 * Robot* obj = robotCreate(width, height);
 * robotStep(obj, num);
 
 * int* param_2 = robotGetPos(obj, retSize);
 
 * char* param_3 = robotGetDir(obj);
 
 * robotFree(obj);
*/
// 最重要的例子：["Robot","getPos", "getDir", "step","getPos","getDir"]
// [[97,98],[],[],[66392],[],[]]

