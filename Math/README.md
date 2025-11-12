
# 🧮 Computational Mathematics & Number Theory

> **System Level:** Cryptographic primitives, hashing algorithms, and O(1) analytical solutions to iterative problems.

---

## 🧠 The Engineering Context

In software engineering, mathematical patterns are often the difference between a "Time Limit Exceeded" and a sub-millisecond solution. While we don't need calculus, we rely heavily on **Discrete Mathematics**.

**Key Engineering Use Cases:**
* **Cryptography:** Modular arithmetic is the foundation of RSA and Elliptic Curve Cryptography.
* **Hashing:** Prime numbers are used in hash functions (e.g., Rolling Hash) to minimize collisions.
* **Distribution:** Combinatorics determine theoretical bounds for load balancing and sharding strategies.

---

## 🛠️ Core Algorithmic Paradigms

### 1. Modular Arithmetic (The Ring $Z_m$)
**Use Case:** preventing Integer Overflow in systems requiring large calculations (e.g., "Count number of ways...").
* **Property:** $(A + B) \pmod M = ((A \pmod M) + (B \pmod M)) \pmod M$
* **Inverse:** Division is complex; we use Modular Inverse (Fermat’s Little Theorem).

### 2. Euclidean Algorithm (GCD)
**Use Case:** Simplifying fractions, finding LCM, rotational array problems.
* **Logic:** `GCD(a, b) = GCD(b, a % b)`
* **Complexity:** $O(\log(\min(a, b)))$. Extremely fast.

### 3. Sieve of Eratosthenes (Prime Generation)
**Use Case:** Finding all primes up to $N$ efficiently.
* **Naive:** Check every number $\to O(N \sqrt{N})$.
* **Sieve:** Mark multiples of each prime as composite $\to O(N \log (\log N))$.

### 4. Boyer-Moore Voting Algorithm
**Use Case:** Finding the majority element (appears $> N/2$ times) in $O(N)$ time and $O(1)$ space.
* **Logic:** Maintain a `candidate` and a `count`. If current number == candidate, `count++`, else `count--`. If `count == 0`, switch candidate.

---

## ⚡ The "Magic" Formulas (Cheatsheet)

Mathematical shortcuts often replace entire loops.

| Concept | Formula / Logic | Complexity |
| :--- | :--- | :--- |
| **Sum of 1..N** | $\frac{N(N+1)}{2}$ | $O(1)$ |
| **LCM(a, b)** | $\frac{|a \cdot b|}{GCD(a, b)}$ | $O(\log N)$ |
| **Divisibility** | A number is prime if not divisible by any $i$ up to $\sqrt{N}$. | $O(\sqrt{N})$ |
| **Catalan Numbers** | Used for BST count, Valid Parentheses count. | $O(N)$ |
| **Digital Root** | `num % 9` (if 0, result is 9) sums digits recursively to 1 digit. | $O(1)$ |

---

## 💻 Universal GCD & LCM Blueprint

Essential for any math-heavy problem.

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // gcd(a, b)
````

-----

## ⚡ Optimization & Safety Checklist

  - [ ] **Integer Overflow:** In languages like Java/C++, `a * b` can exceed $2^{31}-1$. Cast to `long` before multiplying.
  - [ ] **Negative Modulo:** Python handles `-5 % 3 = 1` correctly. C++/Java return `-2`. To fix: `((a % b) + b) % b`.
  - [ ] **Float Precision:** Avoid `float` for equality checks. $0.1 + 0.2 \neq 0.3$ in standard IEEE 754 floating point logic. Use Epsilon comparisons or stick to Integers.
  - [ ] **Corner Cases:** Is `1` a prime? (No). Is `0` a positive number? (No).

-----

## 🧬 Geometry Patterns

Rare but standard.

  * **Point inside Rectangle:** $x_1 \le x \le x_2$ AND $y_1 \le y \le y_2$.
  * **Distance Formula:** Euclidean distance usually involves `sqrt`, which is slow/imprecise. Compare `distance^2` instead to keep integer precision.

<!-- end list -->

```
```
