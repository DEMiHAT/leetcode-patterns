
# 🧬 Bit Manipulation: Hardware-Level Logic

> **System Level:** Direct register manipulation, state compression, and O(1) arithmetic utilizing binary representation.

---

## 🧠 The Engineering Context

Bit Manipulation is the closest an algorithm gets to the hardware. In high-performance systems, bitwise operations are preferred because they execute in a single CPU cycle, unlike expensive arithmetic operations (division/modulo).

**Key Engineering Use Cases:**
* **State Compression:** Packing a boolean array (e.g., `[True, False, True]`) into a single Integer (`101` or `5`), reducing space complexity by factor of 32x or 64x.
* **Masking:** Isolating specific data segments within a packet.
* **XOR Logic:** Efficient toggling and parity checking without conditional branching.

---

## 📟 Register Visualization

Understanding the bitwise layout is mandatory. A standard Integer is 32 bits (4 bytes).

```text
Value: 5 (Decimal)
Binary: 0000 ... 0000 0101
                     ^ ^ ^
        (4) (2) (1) -+ | |
                       | +-- Set Bit (1)
                       +---- Unset Bit (0)
````

-----

## 🛠️ Core Operators & Truth Tables

| Operator | Symbol | Logic | Engineering Application |
| :--- | :---: | :--- | :--- |
| **AND** | `&` | Both `1` → `1` | **Masking** (Extracting specific bits) |
| **OR** | `|` | Either `1` → `1` | **Setting** (Turning bits on) |
| **XOR** | `^` | Different → `1` | **Toggling** / Finding unique elements |
| **NOT** | `~` | Invert | Creating negative masks |
| **L-Shift** | `<<` | Multiply by 2 | Moving bits to significant positions |
| **R-Shift** | `>>` | Divide by 2 | Moving bits to least significant positions |

-----

## 🧩 Common Algorithmic Patterns

### 1\. The XOR Trick (Self-Inverse)

**Property:** `A ^ A = 0` and `A ^ 0 = A`.
**Use Case:** finding the "Single Number" in an array where every other number appears twice.

  * **Logic:** XORing the entire array cancels out duplicates, leaving only the unique element.

### 2\. Masking (Isolating Bits)

**Use Case:** Checking if the $i^{th}$ bit is set.

  * **Formula:** `(num & (1 << i)) != 0`
  * **Logic:** We create a "mask" with a 1 at position $i$ and AND it with the number. If the result is non-zero, the bit was set.

### 3\. Brian Kernighan’s Algorithm

**Use Case:** Counting the number of set bits (population count) efficiently.

  * **Formula:** `n = n & (n - 1)`
  * **Logic:** In every iteration, this operation "turns off" the rightmost set bit. The loop runs exactly $k$ times, where $k$ is the number of set bits (faster than iterating all 32 bits).

-----

## ⚡ The "Magic" Formulas (Cheatsheet)

These constant-time tricks are essential for solving Hard problems efficiently.

| Operation | Formula | Explanation |
| :--- | :--- | :--- |
| **Check Odd/Even** | `(n & 1) == 0` | Checks the Least Significant Bit (LSB). |
| **Get LSB only** | `x & (-x)` | Isolates the rightmost `1`. |
| **Turn off LSB** | `x & (x - 1)` | Flips the rightmost `1` to `0`. |
| **Clear all bits \> i** | `x & ((1 << i) - 1)` | Standard masking technique. |
| **Swap numbers** | `a ^= b; b ^= a; a ^= b` | Swaps without temp variable (in-place). |

-----

## 💻 Universal Blueprint

When solving bitwise problems, we rarely loop $0 \to N$. We loop through the *bits*.

```python
def count_set_bits(n):
    count = 0
    while n > 0:
        n &= (n - 1)  # Drop the lowest set bit
        count += 1
    return count
```

-----

## ⚡ Optimization Checklist

  - [ ] **Operator Precedence:** Bitwise operators (`&`, `|`) often have lower precedence than comparison (`==`). **ALWAYS** wrap bitwise ops in parentheses: `(x & 1) == 0`.
  - [ ] **Signed vs Unsigned:** In Java/C++, be careful with `>>` (arithmetic shift, preserves sign) vs `>>>` (logical shift, fills with zero).
  - [ ] **Overflow:** Shifting `1 << 31` in a signed 32-bit integer can result in a negative number (Two's Complement).

<!-- end list -->

```
```
