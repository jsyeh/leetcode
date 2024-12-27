// LeetCode 3263. Convert Doubly Linked List to Array I
// 把 Doubly Linked List 變成陣列
int* toArray(struct Node *head, int *returnSize) {
    struct Node* now = head;
    int N = 0;
    while(now != NULL) {
        N++;
        now = now->next;
    }
    int* ans = (int*) malloc(sizeof(int)*N);
    for(int i=0; i<N; i++) {
        ans[i] = head->val;
        head = head->next;
    }
    *returnSize = N;
    return ans;
}
/*
// Definition for a Node.
struct Node {
    int val;
    struct Node* next;
    struct Node* prev;
};
*/

