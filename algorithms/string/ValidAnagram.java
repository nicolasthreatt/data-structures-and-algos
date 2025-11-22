/*
Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
    * 1 <= s.length, t.length <= 5 * 104
    * s and t consist of lowercase English letters.

Follow up:
    * What if the inputs contain Unicode characters?
    * How would you adapt your solution to such a case?
*/
package algorithms.string;

import java.util.HashMap;

public class ValidAnagram {

    // Algorithm(s) Used: Two Passes, Hash Map/Set
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        HashMap<Character, Integer> mapper = new HashMap<>();

        for (char letter : s.toCharArray()) {
            if (mapper.containsKey(letter)) {
                mapper.put(letter, mapper.get(letter) + 1);
            } else {
                mapper.put(letter, 1);
            }
        }

        for (char letter : t.toCharArray()) {
            if (mapper.containsKey(letter)) {
                mapper.put(letter, mapper.get(letter) - 1);
            } else {
                mapper.put(letter, 1);
            }
        }

        for (int value : mapper.values()) {
            if (value != 0) return false;
        }

        return true;
    }
}
