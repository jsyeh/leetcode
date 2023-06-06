class MyCalendar {
public:
    vector<int>v1;
    vector<int>v2;
    MyCalendar() {
        
    }
    
    bool book(int start, int end) {
        for(int i=0; i<v1.size(); i++){
            //有兩種狀況是不衝突的 a || b
            //所以衝突就是 !(a||b)
            if( !(end <= v1[i] || v2[i] <= start) ){
                return false;
            }
        }
        v1.push_back(start);
        v2.push_back(end);
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
