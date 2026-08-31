# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Edge case: If there are less than 3 nodes, we can't have any critical points
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_crit = -1
        last_crit = -1
        min_dist = float('inf')
        
        prev = head
        curr = head.next
        idx = 1
        
        while curr.next:
            nxt = curr.next
            
            # Check if the current node is a local maxima or minima
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                if first_crit == -1:
                    first_crit = idx
                else:
                    min_dist = min(min_dist, idx - last_crit)
                
                last_crit = idx
            
            # CRITICAL STEP: Advance the pointers to avoid an infinite loop (TLE)
            prev = curr
            curr = nxt
            idx += 1
            
        # If less than two critical points were found
        if min_dist == float('inf'):
            return [-1, -1]
        
        max_dist = last_crit - first_crit
        
        return [min_dist, max_dist]