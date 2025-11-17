### **Median of Two Sorted Arrays**

#### **Intuition**

This is a challenging problem that requires a time complexity of $O(\log(m+n))$. This logarithmic constraint is a strong hint that we must use **Binary Search**.

A simple merge of the two arrays would be $O(m+n)$, which is too slow.

The **median** is the value that partitions a sorted set into two equal halves. Our goal is to find a "cut" or "partition" in both arrays simultaneously, such that all elements in the combined "left half" are less than or equal to all elements in the combined "right half."

We will perform a binary search on the *smaller* of the two arrays (`nums1`). This search isn't for a *value*, but for the optimal *partition index* (`partition1`).

1.  Let the total length be `total_len = m + n`.
2.  The combined "left half" must contain `half_len = (total_len + 1) // 2` elements.
3.  If we partition `nums1` at `partition1` (taking `partition1` elements for the left half), we must partition `nums2` at `partition2` (taking `partition2` elements), where `partition2 = half_len - partition1`.

Now, we just need to find the `partition1` that makes this a valid median split.

#### **Approach**

The partition is valid if the largest elements on the left are less than or equal to the smallest elements on the right. Since the arrays are sorted, we only need to check the "boundary" elements:

  * `max_left1` (largest from `nums1`'s left half)
  * `min_right1` (smallest from `nums1`'s right half)
  * `max_left2` (largest from `nums2`'s left half)
  * `min_right2` (smallest from `nums2`'s right half)

The partition is correct if: **`max_left1 <= min_right2`** AND **`max_left2 <= min_right1`**.

**Algorithm:**

1.  Ensure `nums1` is the smaller array (if not, swap them). This guarantees our binary search is $O(\log(\min(m, n)))$.
2.  Calculate `total_len = m + n` and `half_len = (total_len + 1) // 2`.
3.  Binary search for `partition1` in `nums1`. The search range is `low = 0` to `high = m`.
4.  In each loop:
      * Set `partition1 = (low + high) // 2`.
      * Calculate `partition2 = half_len - partition1`.
      * Determine the four boundary elements, being careful to use $-\infty$ and $+\infty$ for edge cases (when a partition is 0 or at the end of an array).
5.  **Check the partition:**
      * If `max_left1 > min_right2`: Our `partition1` is too large. Move the search left: `high = partition1 - 1`.
      * If `max_left2 > min_right1`: Our `partition1` is too small. Move the search right: `low = partition1 + 1`.
      * If **both conditions are met**: We found the perfect partition.
          * If `total_len` is **odd**: The median is `max(max_left1, max_left2)`.
          * If `total_len` is **even**: The median is `(max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0`.

#### **Complexity Analysis**

  * **Time Complexity:** $O(\log(\min(m, n)))$
      * We perform a binary search on the *smaller* array. This complexity satisfies the $O(\log(m+n))$ requirement.
  * **Space Complexity:** $O(1)$
      * We only use a few variables for the pointers and boundary values.

-----


### **Problem Link**
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
