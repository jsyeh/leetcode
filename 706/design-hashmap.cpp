// LeetCode 706. Design HashMap
// 用 unordered_map 實作 HashMap
class MyHashMap {
public:
    unordered_map<int, int> myMap;
    MyHashMap() {
        
    }
    
    void put(int key, int value) {
        myMap[key] = value;
    }
    
    int get(int key) {
        if (myMap.find(key)==myMap.end()) return -1;
        return myMap[key];
    }
    
    void remove(int key) {
        if (myMap.find(key)==myMap.end()) return;
        myMap.erase(key);
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
