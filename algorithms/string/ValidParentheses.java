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
package algorithms.string;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class ValidParentheses {

    // Algorithm Used: Hash-Map, Stack (LIFO)
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public boolean isValid(String s) {

        Map<Character, Character> brackets = new HashMap<>();
        brackets.put('{', '}');
        brackets.put('(', ')');
        brackets.put('[', ']');

        // Stack to keep track of opening brackets
        Stack<Character> stack = new Stack<Character>();

        for (char bracket: s.toCharArray()) {
            if(brackets.containsKey(bracket)) {  // If it's an opening bracket, push to stack
                stack.add(bracket);
            } else {  // If there's no opening bracket to match or mismatch found, return False
                if(stack.isEmpty() || (brackets.get(stack.pop()) != bracket)) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
    
}
