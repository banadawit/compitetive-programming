class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # calculate l1
        sum1 = 0
        current_node1 = l1
        power_count1 = 0
        while True:
            sum1 += current_node1.val * 10**power_count1
            if current_node1.next is None:
                break
            current_node1 = current_node1.next
            power_count1 += 1
        
        sum2 = 0
        current_node2 = l2
        power_count2 = 0
        while True:
            sum2 += current_node2.val * 10**power_count2
            if current_node2.next is None:
                break
            current_node2 = current_node2.next
            power_count2 += 1
        
        finalsum = sum1 + sum2
        res = ListNode(finalsum % 10) 
        res_node = res
        while True:
            if finalsum < 10:
                break
            finalsum = int(finalsum / 10)
            res_node.next = ListNode(int(finalsum % 10))
            res_node = res_node.next

        return res
            

        
            
        