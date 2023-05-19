/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int pairSum(struct ListNode* head){
    int N=0;
    struct ListNode* temp = head;

    while( temp!=NULL) {
        N++;
        temp = temp->next;
    }
    //printf("%d\n", N);
    int a[N]; //GNU C++ 的擴充寫法,剛好可以在LeetCode用
    //int *a = (int*)malloc(sizeof(int)*N); //標準的C語言的語法
    temp = head;
    for(int i=0; i<N; i++){
        a[i] = temp->val;
        temp = temp->next;
    }

    int max=0;
    for(int i=0; i<N/2; i++){
        int sum = a[i] + a[N-1-i];
        if(sum>max) max = sum;
    }

    return max;
}
