# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

# 要做多項式的加法（使用Linked List）
class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        head = PolyNode()
        next = head
        while poly1!=None and poly2!=None:
            if poly1.power == poly2.power:
                coef = poly1.coefficient + poly2.coefficient
                if coef != 0: # 這項要留下來
                    temp = PolyNode(coef, poly1.power)
                    next.next = temp
                    next = next.next
                # 不管這項要留下 or 要消滅，接著都處理下一筆
                poly1, poly2 = poly1.next, poly2.next
            elif poly1.power > poly2.power:
                temp = PolyNode(poly1.coefficient, poly1.power)
                next.next = temp
                next = next.next
                poly1 = poly1.next
            else:
                temp = PolyNode(poly2.coefficient, poly2.power)
                next.next = temp
                next = next.next
                poly2 = poly2.next
        # 離開迴圈時，要再把沒算完的接上去
        if poly1 == None and poly2 == None:
            return head.next # 一起完美結束

        if poly2 == None:
            next.next = poly1
        else:
            next.next = poly2
        return head.next
# case 13/52: [[-3,8],[-4,3],[4,2]]
# [[3,8],[7,6],[4,3],[-5,2]]
