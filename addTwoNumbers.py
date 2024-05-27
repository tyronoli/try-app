class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2:
            # Extract values of current nodes
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Create new node with the calculated digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes in both linked lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # If there is a remaining carry, create a new node for it
        if carry:
            current.next = ListNode(carry)

        return dummy_head.next

# Example usage:
# Create linked list 1: 2 -> 4 -> 3 (representing number 342)
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create linked list 2: 5 -> 6 -> 4 (representing number 465)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)  # Resulting linked list represents 342 + 465 = 807
while result:
    print(result.val)
    result = result.next


