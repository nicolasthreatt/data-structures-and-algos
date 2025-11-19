/*
Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    * 1 <= s.length <= 2 * 10^5
    * s consists only of printable ASCII characters.
*/

#include <iostream>
#include <cassert>
#include <cctype>
#include <string>
#include <vector>

using namespace std;

// Algorithm(s) Used: Two Pointers
// Time Complexity: O(n)
// Space Complexity: O(1)
bool isPalindrome(string s) {
    int l = 0;
    int r = s.size();

    while (l < r) {
        while (l < r && !isalnum(s[l])) l += 1;
        while (l < r && !isalnum(s[r])) r -= 1;

        if (tolower(s[l]) != tolower(s[r])) return false;

        l += 1;
        r -= 1;
    }

    return true;
}

int main() {
    vector<pair<string, bool>> test_cases = {
        {"A man, a plan, a canal: Panama", true},
        {"race a car", false},
        {" ", true},
        {"", true},
        {"a", true},
        {"aa", true},
        {"ab", false},
        {"0P", false},
        {"No lemon, no melon", true},
        {"Was it a car or a cat I saw?", true},
        {"12321", true},
        {"1231", false},
        {"!!!", true},
        {"ab@#a", true},
        {"abcba", true},
        {"abccba", true},
        {"abcdba", false},
    };

    for (const auto& tc : test_cases) {
        const string& s = tc.first;
        bool expected = tc.second;
        assert(isPalindrome(s) == expected);
    }
}
