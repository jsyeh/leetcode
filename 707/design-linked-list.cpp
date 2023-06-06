class Node {
public:
    int val;
    Node* next;
    Node(int v) :val(v) {
        //val = v;
        next = nullptr;
    }
};

class MyLinkedList {
public:
    Node root;
    int N = 0;

    MyLinkedList() : root(0), N(0){

    }
    
    int get(int index) {
//printf("get() %d\n", index);
//showList();
        if(index<0 || index>=N) return -1;
        Node* temp = root.next;
        for(int i=0; i<index; i++) {
            temp = temp->next;
//printf("get(index): %d ", temp->val);
        }
//printf("\n");
        return temp->val;
    }
    
    void addAtHead(int val) {
//printf("addAtHead() %d\n", val);
//showList();
        //Node now(val);
        //天啊，意外發現 宣告的物件，在離開時，會被重覆利用。所以要用指標配new
        Node * now = new Node(val);
        now->next = root.next;
        root.next = now;
        N++;
//showList();
    }

    void showList() {
        Node * temp = &root;
        for(int i=0; i<=N; i++){
            printf("i:%d val:%d ", i, temp->val);
            temp = temp->next;
        }
        printf("\n");
    }
    
    void addAtTail(int val) {
//printf("addAtTail() %d\n", val);
//showList();
        Node * temp = &root;
        for(int i=0; i<N; i++) {
//printf("addTail: i:%d val:%d ", i, temp->val);
            temp = temp->next;
        }
//printf("\n");
        //Node now(val);
        Node * now = new Node(val);
        temp->next = now;
        N++;
//showList();
    }
    
    void addAtIndex(int index, int val) {
//printf("addAtIndex() %d %d \n", index, val);
//showList();
        // If index is greater than the length, the node will not be inserted.
        if(index<0 || index>N) return;//如果index是N雖然是範圍外，但剛好是addAtTail()

        Node * temp = &root;
        for(int i=0; i<index; i++) {
            temp = temp->next;
        }
        Node * now = new Node(val);
        now->next = temp->next;
        temp->next = now;
        N++;
//showList();
    }
    
    void deleteAtIndex(int index) {
//printf("deleteAtIndex() %d\n", index);
//showList();
//可能deleteAtIndex()參數不合理時，要提早結束
        if(index>=N || index<0) return;
        Node * temp = &root;
        for(int i=0; i<index; i++) {
            temp = temp->next;
        }//在index的前一項走出來

        if(index!=N-1){//不是最後的 Node，才需要接起來
            Node * one = temp->next;
            temp->next = one->next;
            //free(one);
        }else{
            temp->next = nullptr;
        }
        N--;
//showList();
    }
};
//case 7/65: ["MyLinkedList","addAtTail","get"]
//[[],[1],[0]]
//case 8/65: ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
//[[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]
//可能deleteAtIndex()參數不合理時，要提早結束
//case 48/65: Output Limited Exceeded 不小心印太多內容
//case 62/65: ["MyLinkedList","addAtHead","addAtTail","addAtIndex"]
//[[],[1],[3],[3,2]]


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
