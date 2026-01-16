/*
Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and
finding if a string matches any previously added string.

Implement the WordDictionary class:
    * WordDictionary()
        - Initializes the object.
    * void addWord(word)
        - Adds word to the data structure, it can be matched later.
    * bool search(word)
        - Returns true if there is any string in the data structure that matches word,
          false otherwise.
        - word may contain dots '.' where dots can be matched with any letter.

Example:
    * Input:
        - ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        - [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    * Output:
        - [null,null,null,null,false,true,true,true]

Explanation:
    * WordDictionary wordDictionary = new WordDictionary();
    * wordDictionary.addWord("bad");
    * wordDictionary.addWord("dad");
    * wordDictionary.addWord("mad");
    * wordDictionary.search("pad"); // return False
    * wordDictionary.search("bad"); // return True
    * wordDictionary.search(".ad"); // return True
    * wordDictionary.search("b.."); // return True

Constraints:
    * 1 <= word.length <= 25
    * word in addWord consists of lowercase English letters.
    * word in search consist of '.' or lowercase English letters.
    * There will be at most 2 dots in word for search queries.
    * At most 10^4 calls will be made to addWord and search.
*/

package design;

class Node {
    Node[] children;
    boolean isEndOfWord;

    public Node() {
        children = new Node[26];  // 26 possible children nodes (a-z)
        isEndOfWord = false;      // True if node represent the end of the word
    }
};

public class WordDictionary {

    private Node dictionary;      // Root Node

    public WordDictionary() {
        dictionary = new Node();
    }
    
    // Time Complexity: O(word)
    // Space Compelxity: O(1)
    public void addWord(String word) {
        Node current = dictionary;

        for (char letter : word.toCharArray()) {
            int i = letter - 'a';
            if (current.children[i] == null) {
                current.children[i] = new Node();
            }

            current = current.children[i];
        }

        current.isEndOfWord = true;
    }

    public boolean search(String word) {
        return dfs(word, dictionary);
    }

    // Time Complexity: O(word * 26), when '.' appears. Otherwise, O(word).
    // Space Compelxity: O(word), due to recursion stack usage.
    private boolean dfs(String word, Node node) {
        Node current = dictionary;

        for (int i = 0; i < word.length(); ++i) {
            char letter = word.charAt(i);

            // If the character is '.', it can match any letter:
            //   Recursively search all possible child nodes.
            //   If any recursive call returns True, the word exists.
            if (letter == '.') {
                for (Node child : current.children) {
                    if (child != null && dfs(word.substring(i + 1), child)) {
                        return true;
                    }
                    return false;
                }
            }

            //  Get the index of the character in the alphabet:
            //    If the character does not exist in the trie, return False.
            int key = letter - 'a';
            if (current.children[key] == null) {
                return false;
            }

            current = current.children[key];
        }

        return current.isEndOfWord;
    }
}
