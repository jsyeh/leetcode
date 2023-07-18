//想法1：有個key的ArrayList,每次取過key的話，把key設到最前面？
//但是每次更新時，好像很沒有效率。共有2*10^5呼叫，每次3000格，逐一查看一定超時。
//TODO: 要有資料結構，能快速找到，也快速找到過期的。不能逐一查看
//想法2：想到解法， HashMap 對應到 Node 的 reference, 它有 left,right兩個方向
//所以就把 left 的 right 設成 right, right 的 left 設成 left, 再把挖出來的放到最前面

class LRUCache {
    int N = 0; //current node number
    int c = 0; //capicity
    Node front = new Node(); 
    Node back = new Node();
    HashMap<Integer,Node> map = new HashMap<>();

    public LRUCache(int capacity) {
        front = new Node();
        back = new Node();
        front.right = back;
        back.left = front;
        c = capacity;
    }
    
    public int get(int key) {
System.out.println(N);
        if(!map.containsKey(key)) return -1; //not found
        Node node = map.get(key);
        //把 node 從原地解下來
        Node right = node.right, left = node.left;
        right.left = left; //左右縫起來
        left.right = right; //左右縫起來

        //把 node 移到最前面
        Node first = front.right;
        front.right = node;
        node.left = front;
        first.left = node;
        node.right = first;

        return node.val;
    }
    
    public void put(int key, int value) {
        Node node;
        if(!map.containsKey(key)) {
            node = new Node();
            N++;
        } else {
            node = map.get(key);
            //把 node 從原地解下來
            Node right = node.right, left = node.left;
            right.left = left; //左右縫起來
            left.right = right; //左右縫起來
        }
        //Node node = new Node();//不能直接new它
        node.val = value;
        node.key = key;
        map.put(key, node);//不能直接放它

        //把 node 移到最前面
        Node first = front.right;
        front.right = node;
        node.left = front;
        first.left = node;
        node.right = first;

        if(N>c){ //超過容量，只好吧 last 刪掉
            Node last = back.left, left = last.left;
System.out.println("remove key:"+last.key);
            back.left = left;
            left.right = back; //左右縫起來
            map.remove(last.key); //必須移除，才不會找到殘留的舊值
            N--;
        }
        //} else N++;
    }
    class Node {
        int val, key;
        Node left;
        Node right;
    }
}
//case 13/22: ["LRUCache","put","put","put","put","get","get"]
//[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
//原來，相同的 key 但放不同的值時，要更新它
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
