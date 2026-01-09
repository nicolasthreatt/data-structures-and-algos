/*
Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII.
Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
    - I can be placed before V (5) and X (10) to make 4 and 9. 
    - X can be placed before L (50) and C (100) to make 40 and 90. 
    - C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
    Input: s = "III"
    Output: 3
    Explanation: III = 3.

Example 2:
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.

Example 3:
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
    * 1 <= s.length <= 15
    * s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    * It is guaranteed that s is a valid roman numeral in the range [1, 3999]
*/
#include <cassert>
#include <map>
#include <string>
#include <vector>

using namespace std;

class RomanToInt {
private:
    map<char, int> SYMBOLS_TO_VALUE = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

public:
    // Algorithm(s) Used: Hash Map, Rule-Based Subtraction Logic
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    int romanToIntI(string s) {
        // Base Case - Start with the value of the first Roman numeral
        int total = SYMBOLS_TO_VALUE[s[0]];

        for (int i = 1; i < s.size(); i++) {
            if (s[i - 1] == 'I' && s[i] == 'V') {
                total += SYMBOLS_TO_VALUE[s[i]] - (2 * SYMBOLS_TO_VALUE[s[i - 1]]);
            } else if (s[i - 1] == 'I' && s[i] == 'X') {
                total += SYMBOLS_TO_VALUE[s[i]] - (2 * SYMBOLS_TO_VALUE[s[i - 1]]);
            } else if (s[i - 1] == 'X' && s[i] == 'L') {
                total += SYMBOLS_TO_VALUE[s[i]] - (2 * SYMBOLS_TO_VALUE[s[i - 1]]);
            } else if (s[i - 1] == 'X' && s[i] == 'C') {
                total += SYMBOLS_TO_VALUE[s[i]] - (2 * SYMBOLS_TO_VALUE[s[i - 1]]);
            } else if (s[i - 1] == 'C' && s[i] == 'D') {
                total += SYMBOLS_TO_VALUE[s[i]] - (2 * SYMBOLS_TO_VALUE[s[i - 1]]);
            } else if (s[i - 1] == 'C' && s[i] == 'M') {
                total += SYMBOLS_TO_VALUE[s[i]] - (2 * SYMBOLS_TO_VALUE[s[i - 1]]);
            } else {
                total += SYMBOLS_TO_VALUE[s[i]];
            }
        }

        return total;
    }

    // Algorithm(s) Used: Hash Map, Dynamic Programming (1-D), Bottom-Up, Fibonacci
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    int romanToIntII(string s) {
        // Base Case - Start with the value of the first Roman numeral
        int total = SYMBOLS_TO_VALUE[s[0]]; 

        for (int i = 1; i < s.size(); i++) {
            int prev = SYMBOLS_TO_VALUE[s[i - 1]];
            int curr = SYMBOLS_TO_VALUE[s[i]];

            if (prev < curr) {
                total += curr - (2 * prev);            
            } else {
                total += curr;
            }
        }

        return total;
    }
};

int main() {
    RomanToInt Solution;

    vector<pair<string, int>> test_cases = {
        {"I", 1},
        {"II", 2},
        {"III", 3},
        {"IV", 4},
        {"V", 5},
        {"VI", 6},
        {"IX", 9},
        {"X", 10},
        {"XI", 11},
        {"XIV", 14},
        {"XVIII", 18},
        {"XIX", 19},
        {"XL", 40},
        {"XLIV", 44},
        {"L", 50},
        {"XC", 90},
        {"XCIX", 99},
        {"C", 100},
        {"CD", 400},
        {"D", 500},
        {"CM", 900},
        {"M", 1000},
        {"MCMXCIV", 1994},
        {"MMXXIV", 2024},
    };

    vector<int(RomanToInt::*)(string s)> functions = {
        &RomanToInt::romanToIntI,
        &RomanToInt::romanToIntII,
    };

    for (auto func : functions) {
        for (auto [s, expected] : test_cases) {
            int result = (Solution.*func)(s);
            assert(result == expected);
        }
    }

    return 0;
}
