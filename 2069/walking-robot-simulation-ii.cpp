// LeetCode 2069. Walking Robot Simulation II
// 原本的模擬 874. Walking Robot Simulation 進階，提供工具，讓別人呼叫
// 其實「只會繞四周走」答案是固定的，不用「一步步模擬」
class Robot {
public:
    int circle, i;
    vector<int> x;
    vector<int> y;
    vector<string> dir;
    vector<int> ans;
    Robot(int width, int height) {
        circle = (width+height-2) * 2;
        i = 0;
        for(int xx=1; xx<width; xx++){ // 往東走
            x.push_back(xx);
            y.push_back(0);
            dir.push_back("East");
            i++;
        }
        for(int yy=1; yy<height; yy++){ // 往北走
            x.push_back(width-1);
            y.push_back(yy);
            dir.push_back("North");
            i++;
        }
        for(int xx=width-2; xx>=0; xx--){ // 往西走
            x.push_back(xx);
            y.push_back(height-1);
            dir.push_back("West");
            i++;
        }
        for(int yy=height-2; yy>=0; yy--){ // 往南走
            x.push_back(0);
            y.push_back(yy);
            dir.push_back("South");
            i++;
        }
        i = -1; // 左下角的原點
        ans.push_back(0);
        ans.push_back(0);
    }
    
    void step(int num) {
        i = (i + num) % circle;
    } // 「照著圓周」取「餘數」，直球對決
    
    vector<int> getPos() {
        ans[0] = x[(i+circle)%circle];
        ans[1] = y[(i+circle)%circle];
        return ans;
    }
    
    string getDir() {
        if(i==-1) return string("East"); // 最一開始，是「向東」
        return dir[i];
    }
};

/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */
// 最重要的例子：["Robot","getPos", "getDir", "step","getPos","getDir"]
// [[97,98],[],[],[66392],[],[]]
