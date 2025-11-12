
# 🔗 Linked Lists: Dynamic Memory & Pointer Manipulation

> **System Level:** Non-contiguous heap allocation, reference management, and O(1) structural mutation.

---

## 🧠 The Engineering Context

Unlike Arrays, which require a contiguous block of memory, Linked Lists utilize **Heap Fragmentation**. Each node can exist anywhere in physical memory, connected only by a reference (address) to the next node.

**Key Engineering Trade-offs:**
* **Pros:** Dynamic size (no resizing overhead), $O(1)$ insertion/deletion *if* the pointer is known.
* **Cons:** **Cache Misses** (CPU cannot pre-fetch nodes efficiently), extra memory overhead (storage for the 64-bit address pointer).

**Interview Reality:** Linked List problems are rarely about complex algorithms. They are **Sanity Checks** to ensure you can manipulate pointers without losing track of the `head` or causing a `NullPointerException`.

---

## 📟 Memory Layout Visualization



```text
Heap Memory (Scattered)
+---------+      +---------+      +---------+
| VAL: 10 |  --> | VAL: 20 |  --> | VAL: 30 |  --> NULL
| ADR: 0xA|      | ADR: 0xF|      | ADR: 0x3|
+---------+      +---------+      +---------+
(0x00400)        (0x00912)        (0x00100)
````

-----

## 🛠️ Core Algorithmic Patterns

### 1\. The "Runner" Technique (Fast & Slow Pointers)

**Use Case:** Cycle Detection (Floyd’s Algorithm), Finding the Middle, Kth node from end.

  * **Logic:** Initialize `slow = head` and `fast = head`. Move `slow` by 1 step, `fast` by 2 steps.
  * **Outcome:** If there is a cycle, they will collide. If not, `fast` reaches the end when `slow` is at the middle.
  * **Complexity:** $O(N)$ Time, $O(1)$ Space.

### 2\. The Sentinel Node (Dummy Head)

**Use Case:** Simplifying edge cases where the `head` itself might change (e.g., deleting the first node, merging lists).

  * **Logic:** Create a `dummy` node that points to `head`. Perform operations using `dummy.next`. Return `dummy.next`.
  * **Benefit:** Eliminates the need for `if head is None` checks inside the loop.

### 3\. In-Place Reversal

**Use Case:** Reversing a list or a sub-segment of a list without extra memory.

  * **Logic:** Requires three pointers: `prev`, `curr`, and `next_temp`.
    ```python
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
    ```

-----

## 💻 Universal Traversal Blueprint

Most problems involve traversing while maintaining a specific invariant.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traverse_and_manipulate(head):
    # 1. Sentinel Pattern (Safety)
    dummy = ListNode(0)
    dummy.next = head
    
    # 2. Pointers
    prev = dummy
    curr = head
    
    while curr:
        # 3. Logic (e.g., Delete node if condition met)
        if should_delete(curr.val):
            prev.next = curr.next # Skip current
            # Note: 'prev' stays; 'curr' moves forward
        else:
            prev = curr # Move both
            
        curr = curr.next
        
    return dummy.next
```

-----

## ⚡ Optimization & Safety Checklist

  - [ ] **Lost Head:** Did you accidentally overwrite `head` without saving a reference? (Always use a temporary `curr` pointer for traversal).
  - [ ] **Null Checks:** Always check `if curr is not None` and `if curr.next is not None` before accessing attributes.
  - [ ] **Cycle Death:** In `while` loops involving list mutation, ensure you are actually advancing pointers to avoid infinite loops.
  - [ ] **Memory Leaks:** In C/C++, you must manually `free()` deleted nodes. In Java/Python, ensure no references point to the "deleted" node so GC can sweep it.

-----

## 🔍 Common "Gotchas"

  * **Finding Cycle Start:** After Fast/Slow meet, reset `slow` to `head`. Move both 1 step. The meeting point is the cycle entry.
  * **Merging Sorted Lists:** Use a Dummy node to build the new list tail-first.
  * **Palindrome Check:** Find middle -\> Reverse second half -\> Compare.

<!-- end list -->

```
```
