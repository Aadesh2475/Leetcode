
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, id(head), head))
                
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, id(node.next), node.next))
                
        return dummy.next