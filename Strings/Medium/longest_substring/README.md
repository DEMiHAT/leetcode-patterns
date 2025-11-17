### **Longest Substring Without Repeating Characters**

#### **Intuition**

The problem asks for the length of the *longest* *contiguous* substring that has all unique characters. A brute-force check of all possible substrings would be too slow ($O(n^2)$ or $O(n^3)$).

This problem is a perfect candidate for the **Sliding Window** technique. We can use two pointers, `left` and `right`, to define a "window" `[left...right]` that contains our current substring.

The `right` pointer will expand the window by moving forward. The `left` pointer will contract the window (move forward) only when we find a duplicate character.

To efficiently check for duplicates, we'll use a **Hash Map** (or Dictionary). This map will store each character and the **most recent index** at which it was seen.

#### **Approach (Optimized Sliding Window)**

1.  Initialize a `char_map` (dictionary) to store `char: last_seen_index`.
2.  Initialize `left = 0` (the start of our window) and `max_length = 0`.
3.  Iterate through the string with a `right` pointer from `0` to the end.
4.  Get the character `char = s[right]`.
5.  **Check for duplicate:** If `char` is already in `char_map`, it means we've seen it before.
      * We need to ensure our window starts *after* that previous occurrence.
      * We update `left = max(left, char_map[char] + 1)`.
      * This `max` is crucial: it prevents the `left` pointer from moving *backward* if we find a character whose last occurrence was *before* our current `left` position (e.g., in the string "abba").
6.  **Update Map:** Store the *current* index of `char` in the map: `char_map[char] = right`.
7.  **Calculate Length:** The length of the current valid window is `right - left + 1`. We update our max length: `max_length = max(max_length, right - left + 1)`.
8.  After the loop finishes, return `max_length`.

#### **Complexity Analysis**

  * **Time Complexity:** $O(n)$
      * We iterate through the string once. Both the `left` and `right` pointers only move forward.
      * Hash map lookups and insertions are $O(1)$ on average.
  * **Space Complexity:** $O(\min(n, k))$
      * where $n$ is the length of the string and $k$ is the number of unique characters in the alphabet (e.g., 26 for lowercase English, 128 for ASCII).
      * In the worst case, the map will store all unique characters in the string, up to the size of the alphabet.

-----


### **Problem Link**
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

