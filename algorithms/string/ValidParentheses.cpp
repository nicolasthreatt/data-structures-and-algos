/*
Valid Parentheses
https://leetcode.com/problems/valid-parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Constraints:
    * 1 <= s.length <= 104
    * s consists of parentheses only '()[]{}'.
*/
#include <cassert>
#include <iostream>
#include <map>
#include <stack>
#include <vector>

using namespace std;

// Algorithm(s) Used: Stack
// Time Complexity: O(n)
// Space Complexity: O(n)
bool isValid(string s) {
    map<char, char> brackets;
    brackets.insert({'(', ')'});
    brackets.insert({'{', '}'});
    brackets.insert({'[', ']'});

    stack<char> queue;
    for (char bracket : s) {
        if (brackets.contains(bracket)) {
            queue.push(bracket);
        } else {
            if (queue.empty() || brackets[queue.top()] != bracket) {
                return false;
            }
            queue.pop();
        }
    }

    return queue.empty();
}

int main() {
    assert(isValid("()"));
    assert(isValid("()[]{}"));
    assert(!isValid("(]"));
    assert(isValid("([{}])"));
    assert(!isValid("([)]"));
    assert(!isValid("("));
    assert(!isValid(")"));
    assert(isValid("{[]}"));
    assert(isValid("((({{{[[[]]]}}})))"));
    assert(!isValid("((({{{[[[[]]]}}})))"));

    return 0;
}
