class MyCircularQueue {

    int [] queue;
    int front, rear, capicity, size;
    public MyCircularQueue(int k) {
        queue = new int[k+1];
        front = 0;
        rear = 0;
        capicity = k;
        size = 0;
    }
    
    public boolean enQueue(int value) {
        if(size<capicity) {
            queue[rear] = value;
            rear = (rear+1)%capicity;
            size++;
            return true;
        }
        return false;
    }
    
    public boolean deQueue() {
        if(size>0) {
            front = (front+1)%capicity;//queue[front++];
            size--;
            return true;
        }
        return false;
    }
    
    public int Front() {
        if(size==0) return -1;
        else return queue[front];
    }
    
    public int Rear() {
        if(size==0) return -1;
        else return queue[(rear-1+capicity)%capicity];
    }
    
    public boolean isEmpty() {
        return size==0;
    }
    
    public boolean isFull() {
        return size==capicity;
    }
}
//case 4/58: ["MyCircularQueue","enQueue","enQueue","deQueue","enQueue","deQueue","enQueue","deQueue","enQueue","deQueue", "Front"]
//[[2],[1],[2],[],[3],[],[3],[],[3],[],[]] 陣列用完時，要用 i%capacity 重覆使用

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
