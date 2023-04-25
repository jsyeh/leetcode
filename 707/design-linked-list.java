class MyNode {
    int val;
    MyNode next;
    MyNode prev;
    MyNode(int _val) {val = _val;}
}
class MyLinkedList {
    MyNode head;
    MyNode tail;
    int length = 0;
    public MyLinkedList() {
        head = new MyNode(0);
        tail = new MyNode(0);
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int index) {
        if(index<0 || index>=length) return -1;
        MyNode ans = head.next;
        for(int i=0; i<index; i++){
            ans = ans.next;
        }
        return ans.val;
    }
    
    public void addAtHead(int val) {
        MyNode node = new MyNode(val);
        node.next = head.next;
        head.next.prev = node;

        node.prev = head;
        head.next = node;
        length++;
    }
    
    public void addAtTail(int val) {
        MyNode node = new MyNode(val);
        node.next = tail;
        node.prev = tail.prev;
        tail.prev.next = node;
        tail.prev = node;
        length++;
    }
    
    public void addAtIndex(int index, int val) {
        if(index<0 || index>length) return;
        MyNode node = new MyNode(val);
        MyNode prev = head;
        for(int i=0; i<index; i++){
            prev = prev.next;
        }
        node.prev = prev;
        node.next = prev.next;
        prev.next.prev = node;
        prev.next = node;
        length++;
    }
    
    public void deleteAtIndex(int index) {
        if(index<0 || index>=length) return;
        MyNode prev = head;
        for(int i=0; i<index; i++){
            prev = prev.next;
        }
        MyNode next = prev.next.next;
        prev.next = next;
        next.prev = prev;

        length--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
