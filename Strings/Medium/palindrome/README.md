

### **Longest Palindromic Substring**

#### **Intuition**

A brute-force approach would be to check every possible substring ($O(n^2)$ substrings) and, for each one, check if it's a palindrome (an $O(n)$ operation). This $O(n^3)$ solution is too slow.

A more efficient method is the **"Expand From Center"** technique. A palindrome is a string that is symmetrical around its center. This center can be one of two things:

1.  A single character (for odd-length palindromes, like "a**b**a").
2.  The space between two characters (for even-length palindromes, like "a**bb**a").

There are $n$ potential single-character centers and $n-1$ potential two-character centers. We can iterate through all $2n - 1$ possible centers, and for each one, "expand" outwards (one pointer moving left, one moving right) as long as the characters match. We keep track of the longest palindrome we've found so far.

#### **Approach**

1.  Initialize `start` and `end` variables to `0`. These will store the indices of the longest palindrome found.
2.  Iterate through the string with an index `i` from `0` to `n-1`.
3.  For each `i`, check both possible centers:
      * **Odd-length center:** Call a helper function `expand(s, i, i)` to find the longest palindrome centered at `i`.
      * **Even-length center:** Call the same helper `expand(s, i, i + 1)` to find the longest palindrome centered between `i` and `i+1`.
4.  Compare the lengths from these two calls (`len1` and `len2`) and take the maximum `length`.
5.  If this new `length` is greater than the current `end - start`, update `start` and `end` to reflect the new longest palindrome.
      * The new `start` is `i - (length - 1) // 2`.
      * The new `end` is `i + length // 2`.
6.  After the loop finishes, return the slice `s[start : end + 1]`.

**Helper Function `expand(s, left, right)`:**

  * This function takes the string and two starting pointers (which are the same for odd centers, and `i, i+1` for even centers).
  * It runs a `while` loop: `while left >= 0 and right < len(s) and s[left] == s[right]`:
      * `left -= 1`
      * `right += 1`
  * Once the loop breaks, the pointers are one position *outside* the palindrome. The actual length is `right - left - 1`.
  * Return this length.

#### **Complexity Analysis**

  * **Time Complexity:** $O(n^2)$
      * We have $O(n)$ potential centers. The "expand" operation from each center can take up to $O(n)$ time in the worst case (e.g., a string like "aaaaaaaa").
  * **Space Complexity:** $O(1)$
      * We only use a few variables to store the `start` and `end` indices, requiring constant extra space.

-----




### **Problem Link**
https://leetcode.com/problems/longest-palindromic-substring/description/
