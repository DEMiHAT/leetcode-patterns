import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
            
        total_len = m + n
        half_len = (total_len + 1) // 2
        
        low = 0
        high = m 
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = half_len - partition1
            
         
            
            max_left1 = nums1[partition1 - 1] if partition1 > 0 else -math.inf
            max_left2 = nums2[partition2 - 1] if partition2 > 0 else -math.inf
            
            
            min_right1 = nums1[partition1] if partition1 < m else math.inf
            min_right2 = nums2[partition2] if partition2 < n else math.inf
            
           
            
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                
                if total_len % 2 == 1:
                    
                    return max(max_left1, max_left2)
                else:
                    
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            
            elif max_left1 > min_right2:
                
                high = partition1 - 1
            else:
               
                low = partition1 + 1
                
        return 0.0 