
### **Add Two Numbers**

#### **Intuition**
The problem asks us to add two numbers represented by linked lists, where the digits are stored in **reverse order**. This reverse storage is actually very convenient because it mimics the way we perform addition manually on paper: we start from the "ones" column (the least significant digit) and move towards the left, carrying over any excess value to the next position.



We can simulate this column-by-column addition by traversing both linked lists simultaneously. We keep track of a `carry` value (initially 0) and add it to the sum of the current nodes from both lists. If one list is shorter than the other, we can treat the missing nodes as having a value of `0`.

#### **Approach**
1.  **Initialize Pointers:** Create a `dummy_head` node to simplify edge cases (like handling the head of the result list) and a `current` pointer to build the new list. Initialize a variable `carry` to 0.
2.  **Traverse Lists:** Loop as long as there is a node left in `l1`, a node left in `l2`, or a non-zero `carry`.
3.  **Calculate Sum:**
    * Extract values from the current nodes of `l1` and `l2`. If a list has reached the end (is `None`), use `0` as the value.
    * Compute `total = val1 + val2 + carry`.
4.  **Update Carry and Result:**
    * Update `carry` for the next iteration: `carry = total // 10`.
    * Create a new node with the digit value `total % 10` and attach it to `current.next`.
5.  **Move Pointers:** Advance `current`, `l1`, and `l2` pointers.
6.  **Return:** Return `dummy_head.next` (the actual head of the result list).

#### **Complexity Analysis**

* **Time Complexity:** $O(\max(M, N))$
    * where $M$ and $N$ are the lengths of the two linked lists. We traverse the lists exactly once, and the loop runs for the length of the longer list.
* **Space Complexity:** $O(\max(M, N))$
    * The length of the new list is at most $\max(M, N) + 1$.

---

### **Problem Link**

