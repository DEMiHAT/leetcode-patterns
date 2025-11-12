

````markdown
# ⚡ Arrays: Contiguous Memory & Iterative Logic

> **System Level:** Direct memory access, cache locality optimization, and pointer arithmetic.

---

## 🧠 The Engineering Context

In high-performance computing, Arrays are the king of data structures due to **Spatial Locality**. Unlike Linked Lists, array elements are stored contiguously in RAM, allowing the CPU to pre-fetch data efficiently into the cache lines.

**Key Objectives in this Module:**
* **Minimizing State:** Solving problems in-place ($O(1)$ Space) rather than allocating new buffers.
* **Traversal Efficiency:** Reducing quadratic nested loops ($O(N^2)$) to linear ($O(N)$) using pointer manipulation.
* **Hashing Trade-offs:** utilizing space-time trade-offs to achieve $O(1)$ lookups.

---

## 📟 Memory Layout Visualization

Understanding the underlying memory structure is crucial for index manipulation.

```text
[ADDR 0x00] [ADDR 0x04] [ADDR 0x08] [ADDR 0x0C]  <-- Physical Memory
+---------+ +---------+ +---------+ +---------+
|  VAL 0  | |  VAL 1  | |  VAL 2  | |  VAL 3  |  <-- Contiguous Block
+---------+ +---------+ +---------+ +---------+
     ^           ^
     |           |
   Index i     Index j (O(1) Access Time)
````

-----

## 🛠️ Core Algorithmic Strategies

We do not memorize solutions; we apply **patterns**. Here are the primary mental models used in this directory:

### 1\. The Sliding Window (Adaptive Buffer)

  * **Concept:** Converting a nested loop structure into a single pass by maintaining a dynamic range `[left, right]`.
  * **Application:** Subarrays of size `K`, Longest substring without repeats.
  * **Visual:**
    ```text
    [ a, b, { c, d, e }, f, g ]  --> Expand Right
    [ a, b, c, { d, e, f }, g ]  --> Shrink Left
    ```

### 2\. Two Pointers (Convergence)

  * **Concept:** Utilizing sorted data properties or swapping logic to process data from both ends simultaneously.
  * **Application:** 3Sum, Container With Most Water, Trapping Rain Water.
  * **Complexity:** Typical reduction from $O(N^2)$ to $O(N)$.

### 3\. Prefix State (Pre-computation)

  * **Concept:** Storing the cumulative state of the array up to index `i` to answer range queries in $O(1)$.
  * **Math:** `RangeSum(i, j) = Prefix[j] - Prefix[i-1]`

-----

## ⚡ Optimization Checklist

Before marking a problem as "Solved," the following optimizations are verified:

  - [ ] **Sanity Check:** Are boundaries (`< 0` or `>= length`) handled?
  - [ ] **In-Place Swap:** Can we overwrite the input array to save space?
  - [ ] **Lookup Speed:** Is a `HashMap` ($O(1)$) better than a nested search ($O(N)$)?
  - [ ] **Overflow:** For integer operations, is there a risk of exceeding `MAX_INT`?

-----

## 🧬 Generic Pattern Blueprint

Most array problems in this repository follow this structural skeleton:

```python
def flexible_window_pattern(nums):
    start = 0
    current_result = 0
    
    # 1. LINEAR SCAN (The "Expander")
    for end in range(len(nums)):
        # 2. INGEST DATA
        add_to_state(nums[end])
        
        # 3. CONTRACT WINDOW (The "Optimizer")
        while constraint_broken():
            remove_from_state(nums[start])
            start += 1
            
        # 4. CAPTURE METRIC
        current_result = max(current_result, end - start + 1)
        
    return current_result
```

```
```
