
# 🔡 Strings: Immutable Sequences & Lexicographical Parsing

> **System Level:** Buffer handling, character encoding standards (ASCII/UTF-8), and prefix-tree optimization structures.

---

## 🧠 The Engineering Context

In high-level languages (Java, Python, C#), Strings are often **Immutable**. This design choice ensures thread safety and enables the **String Constant Pool**, but it introduces massive performance pitfalls if mishandled.

**Key Engineering Trade-offs:**
* **The Concatenation Trap:** Doing `s = s + "c"` inside a loop creates a new object every iteration, degrading complexity to $O(N^2)$.
* **Solution:** Always use Mutable Buffers (`StringBuilder` in Java, `list` in Python) to maintain $O(N)$ appending.
* **Encoding:** Understanding that a `char` is not always 1 byte (UTF-8 variable length) is critical for internationalization (i18n).

---

## 🛠️ Core Algorithmic Paradigms

### 1. The Frequency Map (Counter)
**Use Case:** Anagrams, Permutations, Ransom Note.
* **Logic:** Strings are just arrays of integers (ASCII values).
* **Optimization:** Instead of a generic `HashMap` (high overhead), use a fixed-size integer array `int[26]` for lowercase English letters.
* **Space Complexity:** Reduces from generic heap allocation to $O(1)$ (fixed 104 bytes).

### 2. Sliding Window (Substring Search)
**Use Case:** Longest Substring Without Repeating Characters, Minimum Window Substring.
* **Logic:** Expand the `right` pointer to ingest characters. If constraints are violated (e.g., duplicate found), increment `left` to shrink window until valid.

### 3. Trie (Prefix Tree)
**Use Case:** Autocomplete, Spell Checker, IP Routing.
* **Logic:** Instead of storing full strings, we store characters as nodes in a tree.
* **Benefit:** Search complexity depends on *word length* $L$, not the number of words $N$. Lookup is $O(L)$.

### 4. Rolling Hash (Rabin-Karp)
**Use Case:** Plagiarism detection, DNA sequencing.
* **Logic:** Calculate the hash of a window. When sliding the window, remove the leading char's value and add the trailing char's value in $O(1)$ math, rather than rehashing the whole string.

---

## 📟 Pattern Matching Complexity

| Algorithm | Time Complexity | Space | Application |
| :--- | :--- | :--- | :--- |
| **Brute Force** | $O(N \cdot M)$ | $O(1)$ | Simple scripts. |
| **KMP** | $O(N + M)$ | $O(M)$ | Search in text editors (uses LPS array). |
| **Rabin-Karp** | $O(N + M)$ (Avg) | $O(1)$ | Multiple pattern search. |
| **Trie Traversal** | $O(L)$ | $O(N \cdot L)$ | Dictionary/Autocomplete. |

---

## 💻 Universal Anagram/Frequency Blueprint

80% of "Easy/Medium" string problems are solved by counting characters.

```python
def solve_string_frequency(s, t):
    if len(s) != len(t): return False
    
    # 1. Fixed Size Array (Optimization over HashMap)
    count = [0] * 26 
    
    # 2. Net Zero Logic
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
        
    # 3. Validation
    for val in count:
        if val != 0: return False
        
    return True
````

-----

## ⚡ Optimization & Safety Checklist

  - [ ] **StringBuilder:** Are you using string concatenation `+=` in a loop? Refactor to `join()` or `StringBuilder` immediately.
  - [ ] **Corner Cases:** Empty strings `""`, Single character `"a"`, Strings with only spaces `"   "`.
  - [ ] **Case Sensitivity:** Does "A" == "a"? Usually, you need `.lower()` or case-insensitive comparators.
  - [ ] **Key Uniqueness:** When using Strings as HashMap keys, remember that computing the Hash Code takes $O(L)$ time (where L is string length). It is NOT $O(1)$.

-----

## 🧬 Advanced Structure: The Palindrome

  * **Center Expansion:** To find the longest palindrome, iterate through the string and treat every character (and every gap between characters) as the "center," expanding outwards.
  * **Manacher's Algorithm:** solves Longest Palindromic Substring in strictly $O(N)$ (Overkill for interviews, but good for trivia).

<!-- end list -->

```
```
