
# 💾 Dynamic Programming: Caching & State Optimization

> **Algorithmic Paradigm:** Recursion + Memoization. Breaking complex problems into overlapping sub-problems and caching the results to avoid redundant computation.

---

## 🧠 The Engineering Context

Dynamic Programming (DP) is the ultimate **Space-Time Tradeoff**. In systems engineering, this is analogous to adding a **Cache Layer** (like Redis) in front of a database. We spend a little extra memory (RAM) to store results so we never calculate the same thing twice.

**The Transformation:**
* **Naive Recursion:** $O(2^N)$ (Exponential - Unusable for $N > 40$)
* **With DP:** $O(N)$ or $O(N^2)$ (Polynomial - Instant)

**Key Engineering Principles:**
* **Optimal Substructure:** The solution to a large problem can be built from solutions to smaller problems.
* **Overlapping Subproblems:** The recursion tree visits the same state multiple times (this is where we optimize).

---

## 📉 Visualizing the Optimization

We transform a deep, branching recursion tree into a flat, iterative lookup table.

**The Fibonacci Example ($F_5$):**

```text
WITHOUT DP (Recursion)           WITH DP (Memoization/Tabulation)
       F(5)                      [ 0, 1, 1, 2, 3, 5 ]
      /    \                       ^  ^  ^  ^  ^  ^
   F(4)    F(3)                    |  |  |  |  |  |
   /  \    /  \                   F0 F1 F2 F3 F4 F5
 F(3) F(2) F(2) F(1) ...
  ^    ^    ^
  |____|____|
(Repeated Work = Waste)          (Linear Access = O(1))
````

-----

## 🛠️ Core Patterns & Frameworks

DP is not about guessing; it is about defining the **State** and the **Transition**.

### 1\. 1D Dynamic Programming (Linear)

**Use Case:** "Count ways to reach N", "Max profit over time".

  * **State:** `dp[i]` = best result at index `i`.
  * **Transition:** `dp[i] = dp[i-1] + dp[i-2]` (e.g., Climbing Stairs).
  * **Space Optimization:** Usually reducible to $O(1)$ variables since we only need the previous 1 or 2 states.

### 2\. The Knapsack Pattern (0/1 & Unbounded)

**Use Case:** Resource allocation constraints. "Maximize value V given capacity W".

  * **State:** `dp[i][w]` = Max value considering first `i` items with weight limit `w`.
  * **Logic:** At every item, we ask: **"Include it or Exclude it?"**
  * **Transition:** `dp[w] = max(dp[w], price + dp[w - weight])`.

### 3\. Longest Common Subsequence (LCS)

**Use Case:** String matching, diff tools (git), DNA sequencing.

  * **State:** `dp[i][j]` = LCS of `stringA[0...i]` and `stringB[0...j]`.
  * **Logic:** If characters match, `1 + diagonal`. If not, `max(up, left)`.

### 4\. Palindromes & Intervals

**Use Case:** Matrix Chain Multiplication, Longest Palindromic Substring.

  * **Logic:** We expand around a center or process intervals `(i, j)` based on `(i+1, j-1)`.

-----

## ⚡ The Universal DP Framework (4 Steps)

Do not write code immediately. Follow this derivation process:

1.  **Define the State:** What variables uniquely identify a scenario? (e.g., `index`, `capacity`, `is_holding_stock`).
2.  **Formulate the Recurrence:** Mathematically relate the current state to previous states.
      * *Example:* $f(n) = \text{cost}[n] + \min(f(n-1), f(n-2))$
3.  **Identify Base Cases:** When does the recursion stop? (e.g., `index < 0` or `sum == 0`).
4.  **Decide Approach:**
      * **Top-Down (Memoization):** Recursive + HashMap. Easier to write.
      * **Bottom-Up (Tabulation):** Iterative Array. Better space complexity (no stack overflow).

-----

## 💻 Code Template: Top-Down Memoization

```python
def solve_dp(items, capacity):
    memo = {}

    def recurse(index, remaining_cap):
        # 1. Base Cases
        if index >= len(items) or remaining_cap == 0:
            return 0
            
        # 2. Check Cache
        state = (index, remaining_cap)
        if state in memo:
            return memo[state]
        
        # 3. Recurrence (Decision Logic)
        # Option A: Skip item
        exclude = recurse(index + 1, remaining_cap)
        
        # Option B: Take item (if it fits)
        include = 0
        if items[index].weight <= remaining_cap:
            include = items[index].value + recurse(index + 1, remaining_cap - items[index].weight)
            
        # 4. Cache & Return
        memo[state] = max(exclude, include)
        return memo[state]

    return recurse(0, capacity)
```

-----

## ⚡ Optimization Checklist

  - [ ] **Space Reduction:** Can `dp[n][m]` be reduced to `dp[m]` (1D array)? (Usually yes, if we only look at the previous row).
  - [ ] **Integer Overflow:** In "Count Ways" problems, results explode quickly. Do we need `% 10^9 + 7`?
  - [ ] **Base Case Validity:** Did we initialize the DP array with `0`, `-1`, or `Infinity` depending on the goal (Max vs Min)?

<!-- end list -->

```
```
