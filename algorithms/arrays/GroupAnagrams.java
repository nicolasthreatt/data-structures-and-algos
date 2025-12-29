/*
Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    * 1 <= strs.length <= 10^4
    * 0 <= strs[i].length <= 100
    * strs[i] consists of lowercase English letters.
*/

package algorithms.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class GroupAnagrams {

    // Algorithm(s) Used: Hash Map
    // Time Complexity: O(n*klog(k))
    // Space Complexity: O(n)
    public List<List<String>> groupAnagramsI(String[] strs) {
        HashMap<String, List<String>> anagrams = new HashMap<>();

        for (String anagram : strs) {
            char[] chars = anagram.toCharArray();
            Arrays.sort(chars);

            String key = new String(chars);  // Strings are Immutable Objects

            anagrams.computeIfAbsent(key, k -> new ArrayList<>()).add(anagram);
        }

        return new ArrayList<>(anagrams.values());
    }

    // Algorithm(s) Used: Hash Map, Bucketing
    // Time Complexity: O(n*k)
    // Space Complexity: O(n)
    public List<List<String>> groupAnagramsII(String[] strs) {
        HashMap<String, List<String>> anagrams = new HashMap<>();

        for (String anagram : strs) {
            int[] chars = new int[26];  // Bucket (frequency cont) for each character

            for (int k = 0; k < anagram.length(); k++) {
                chars[anagram.charAt(k) - 'a']++;
            }

            String key = Arrays.toString(chars);  // Strings are Immutable Objects

            anagrams.putIfAbsent(key, new ArrayList<>());
            anagrams.get(key).add(anagram);
        }

        return new ArrayList<>(anagrams.values());
    }
}
