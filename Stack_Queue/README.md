
# 📚 Stacks & Queues: Sequential Buffer Management

> **System Level:** LIFO/FIFO data flow control, monotonic state tracking, and recursive emulation.

---

## 🧠 The Engineering Context

While Arrays allow random access, Stacks and Queues enforce **Temporal Ordering**. In systems design, they are the gatekeepers of processing logic.

**Key Engineering Use Cases:**
* **Stack (LIFO):** The OS Call Stack, Browser History (Back/Forward), Syntax Parsing (Compiler brackets), Undo/Redo operations.
* **Queue (FIFO):** Job Scheduling (Printer/CPU), Message Brokers (Kafka/RabbitMQ), Breadth-First Search (BFS).
* **Deque (Double-Ended):** Sliding Window Maximums ($O(N)$), Work Stealing algorithms.

---

## 📟 Data Flow Visualization

Understanding the restriction on access points is key.

```text
      STACK (LIFO)                 QUEUE (FIFO)
    |             |             [ IN ] ---------> [ OUT ]
    | [ Element ] | <--- Top      ^                 |
    | [ Element ] |               |_________________|
    | [ Element ] |             (Enqueue)        (Dequeue)
    +-------------+
````

-----

## 🛠️ Core Algorithmic Paradigms

### 1\. The Monotonic Stack

**Use Case:** "Next Greater Element", "Daily Temperatures", "Largest Rectangle in Histogram".

  * **Concept:** Maintaining a stack that is always sorted (increasing or decreasing).
  * **Logic:** Before pushing a new element `X`, pop all elements smaller than `X`. The element that remains at the top is the "Next Greater".
  * **Complexity:** Reduces brute force $O(N^2)$ to $O(N)$ (each element pushed/popped at most once).

### 2\. Parentheses & Parsing

**Use Case:** Valid Parentheses, Calculator implementation.

  * **Logic:** When encountering an opening bracket `(`, push to stack. When closing `)`, check if the top matches. If stack is empty at end, valid.

### 3\. Queue for BFS (Level Order)

**Use Case:** Shortest path in unweighted graphs, Rotting Oranges.

  * **Logic:** Process nodes in layers. Current layer nodes add their neighbors to the back of the queue.

### 4\. Monotonic Deque (Sliding Window)

**Use Case:** "Sliding Window Maximum".

  * **Logic:** Store indices in a Deque. Remove indices from the *back* if they are smaller than the current element (useless). Remove indices from the *front* if they are out of the window range.
  * **Result:** The front of the Deque always holds the maximum of the current window.

-----

## 💻 Universal Monotonic Stack Blueprint

This template solves almost every "Find the next/previous larger/smaller element" problem.

```python
def solve_monotonic_stack(nums):
    stack = [] # Stores indices
    result = [-1] * len(nums)
    
    for i, current_val in enumerate(nums):
        # While stack is not empty AND current val beats top of stack
        while stack and nums[stack[-1]] < current_val:
            index = stack.pop()
            result[index] = current_val # We found the "Next Greater"
            
        stack.append(i)
        
    return result
```

-----

## ⚡ Optimization & Safety Checklist

  - [ ] **Empty Stack Exception:** Always check `if not stack.isEmpty()` before calling `.pop()` or `.peek()`.
  - [ ] **Language Specifics:**
      - **Java:** Use `ArrayDeque` instead of `Stack` (Legacy class, slow).
      - **Python:** Use `List` (`append`/`pop`) for Stack. Use `collections.deque` for Queue ($O(1)$ popleft).
  - [ ] **Circular Queue:** In embedded systems (fixed buffer size), standard queues waste space. Use modulo arithmetic `(i + 1) % capacity` to wrap around.

-----

## 📉 Complexity Reality

| Operation | Array | LinkedList | Stack/Queue |
| :--- | :--- | :--- | :--- |
| **Access (i)** | $O(1)$ | $O(N)$ | N/A |
| **Search** | $O(N)$ | $O(N)$ | N/A |
| **Insert/Delete** | $O(N)$ | $O(1)$ | **$O(1)$** |

*Note: Stacks and Queues are optimized purely for insertion/deletion at the ends. If you need to search inside them, you are using the wrong data structure.*

```
```
