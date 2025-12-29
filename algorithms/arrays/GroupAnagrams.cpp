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

#include <cassert>
#include <cstring>
#include <unordered_map>
#include <vector>

using namespace std;

class GroupAnagrams {
public:

    // Algorithm(s) Used: Hash Map
    // Time Complexity: O(n*klog(k))
    // Space Compexity: O(n)
    vector<vector<string>> groupAnagramsI(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;

        for (const string& anagram : strs) {
            string key = anagram;  // String are Immutable Objects
            sort(key.begin(), key.end());

            anagrams[key].push_back(anagram);         
        }

        vector<vector<string>> solution;
        solution.reserve(anagrams.size());  // Only allocates memory

        for (const auto& pair : anagrams) {
            solution.push_back(pair.second);
        }

        return solution;
    }

    // Algorithm(s) Used: Hash Map, Bucketing
    // Time Complexity: O(n*k)
    // Space Compexity: O(n)
    vector<vector<string>> groupAnagramsII(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;  // Strings are Immutable Objects

        for (const string& anagram: strs) {
            vector<int> chars(26, 0);
            string key;

            // Count letters
            for (char letter : anagram) {
                chars[letter - 'a']++;  // Bucket (frequency cont) for each character
            }

            // Encode key
            for (int frequency : chars) {
                key += '#';  // Seperator so that 1,11 != 11,1
                key += to_string(frequency);
            }

            anagrams[key].push_back(anagram);
        }

        vector<vector<string>> solution;
        solution.reserve(anagrams.size());

        for (const auto& pair : anagrams) {
            solution.push_back(pair.second);
        }

        return solution;
    }
};

int main() {
    GroupAnagrams Solution;

    // (input, expected)
    vector<tuple<vector<string>, vector<vector<string>>>> test_cases = {
        {{"eat", "tea", "tan", "ate", "nat", "bat"}, {{"eat","tea","ate"}, {"tan","nat"}, {"bat"}}},
        { {""}, { {""} } },
        { {"a"}, { {"a"} } },
        { {"abc","bca","cab","xyz","zyx"}, { {"abc","bca","cab"}, {"xyz","zyx"} } },
        { {"listen","silent","enlist","google","gogole"}, { {"listen","silent","enlist"}, {"google","gogole"} } }
    };

    vector<vector<vector<string>> (GroupAnagrams::*)(vector<string>&)> funcs = {
        &GroupAnagrams::groupAnagramsI,
        &GroupAnagrams::groupAnagramsII
    };

    for (auto func : funcs) {
        for (auto& tc : test_cases) {
            vector<string> strs;
            vector<vector<string>> expected;
            tie(strs, expected) = tc;

            vector<vector<string>> result = (Solution.*func)(strs);

            for (auto &group : result) sort(group.begin(), group.end());
            for (auto &group : expected) sort(group.begin(), group.end());

            sort(result.begin(), result.end());
            sort(expected.begin(), expected.end());

            assert(result == expected);
        }
    }

    return 0;
}
