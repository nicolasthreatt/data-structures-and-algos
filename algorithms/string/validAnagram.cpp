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
#include <cassert>
#include <map>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

// Algorithm(s) Used: Two Passes, Hash Map/Set
// Time Complexity: O(n)
// Space Complexity: O(n)
bool isAnagram(string s, string t) {
    if (s.size() != t.size()) return false;

    map<char, int> mapper;

    for (char letter : s) {
        if (mapper.contains(letter)) {
            mapper[letter] += 1;
        } else {
            mapper[letter] = 1;
        }
    }

    for (char letter : t) {
        if (mapper.contains(letter)) {
            mapper[letter] -= 1;
        } else {
            mapper[letter] = 1;
        }
    }

    for (const auto& [key, value] : mapper) {
        if (value != 0) {
            return false;
        }
    }

    return true;
}


int main() {
    vector<tuple<string, string, bool>> test_cases = {
        {"anagram", "nagaram", true},
        {"rat", "car", false},
        {"a", "a", true},
        {"ab", "ba", true},
        {"abc", "ab", false},
        {"aa", "bb", false},
        {"listen", "silent", true},
    };

    vector<bool(*)(string, string)> funcs = {
        isAnagram,
    };

    for (auto func : funcs) {
        for (auto &tc : test_cases) {
            string s, t;
            bool expected;
            tie(s, t, expected) = tc;
            assert(func(s, t) == expected);
        }
    }

    return 0;
}
