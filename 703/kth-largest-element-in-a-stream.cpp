class KthLargest {
public:
    //本題,要找第k大的數字
    int k2;
    //vector<int> all;
    priority_queue<int, vector<int>, greater<int>> all;

    KthLargest(int k, vector<int>& nums) {
        k2 = k;//備份一下k
        for(int i=0; i<nums.size(); i++){
            all.push( nums[i] );
            if(all.size()>k2) all.pop(); //超過數量,就丟
        }//備份好全部的數字
    }
    
    int add(int val) {
        all.push(val);
        if(all.size()>k2) all.pop(); //超過數量,就丟
        //sort(all.begin(), all.end()); //從小到大排好(比較沒有效率)
        //最出第k大的數字 (我們記成 k2)
        return all.top(); //return all[ all.size() - k2 ];//return all[k2];不行,因為all是小到大,我們要大到小
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
