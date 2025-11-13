### **Two Sum**

#### **Intuition**
The brute force approach involves checking every pair of numbers to see if they sum to the target, which results in a slow quadratic time complexity. To optimize this, we can utilize a **Hash Map** (Dictionary) to "remember" the numbers we have already seen.

As we iterate through the array, for every number `num`, we calculate the `complement` needed to reach the `target` (`complement = target - num`). If this `complement` is already in our map, we have found the solution. This allows us to solve the problem in a single pass, trading space complexity for significantly faster time complexity.

#### **Approach**
1.  Initialize an empty hash map to store the mapping of `value -> index`.
2.  Iterate through the array of numbers only once.
3.  For each current `num`, calculate the required value: `complement = target - num`.
4.  Check if the `complement` exists in the hash map:
    * **If it exists:** We found the pair. Return the index of the complement (retrieved from the map) and the current index.
    * **If it does not exist:** Store the current `num` as a key and its index `i` as the value in the map for future lookups.

#### **Complexity Analysis**

* **Time Complexity:** $O(n)$
    * We traverse the list containing $n$ elements exactly once.
    * Hash map lookups and insertions take $O(1)$ time on average.
* **Space Complexity:** $O(n)$
    * In the worst-case scenario (where the pair is at the end or no pair exists), we store $n$ elements in the hash map.
 
### **Problem Link**
https://leetcode.com/problems/two-sum/description/

---


