/*
Implement Trie Prefisx Tree
https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data structure used
to efficiently store andretrieve keys in a dataset of strings.

There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
    - Trie():
        + Initializes the trie object.
    - void insert(String word):
        + Inserts the string word into the trie.
    - boolean search(String word):
        + Returns true if the string word is in the trie (i.e., was inserted before),
          and false otherwise.
    - boolean startsWith(String prefix)
        + Returns true if there is a previously inserted string word that has the prefix prefix,
          and false otherwise.

Input:
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output:
    [null, null, true, false, true, null, true]

Explanation:
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True

Constraints:
    * 1 <= word.length, prefix.length <= 2000
    * word and prefix consist only of lowercase English letters.
    * At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
*/

package design;

class TrieNode {
    TrieNode[] children;
    boolean isEndOfWord;

    public TrieNode() {
        children = new TrieNode[26];  // 26 possible children nodes (a-z)
        isEndOfWord = false;          // True if node represent the end of the word
    }
};

public class Trie {

    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode current = root;

        // Iterate through each character in the word:
        //   Get the index of the character in the alphabet
        //   If the character does not exist in the trie, create a new node
        //   Update the current node to the next node
        for (char letter : word.toCharArray()) {
            int i = letter - 'a';
            if (current.children[i] == null) {
                current.children[i] = new TrieNode();
            }
            current = current.children[i];
        }

        // Mark the last node as the end of the word
        current.isEndOfWord = true;
    }

    public boolean search(String word) {
        TrieNode current = root;

        // Iterate through each character index in the word:
        //   If the character does not exist in the trie, return False.
        //   If the character exists in the trie, update the current node to the next node.
        for (char letter : word.toCharArray()) {
            int i = letter - 'a';
            if (current.children[i] == null) {
                return false;
            }
            current = current.children[i];
        }

        // Mark the last node as the end of the word
        return current.isEndOfWord;
    }

    public boolean startsWith(String prefix) {
        TrieNode current = root;

        // Iterate through each character in the prefix:
        //   If the character does not exist in the trie, return False.
        //   If the character exists in the trie, update the current node to the next node.
        for (char letter : prefix.toCharArray()) {
            int i = letter - 'a';
            if (current.children[i] == null) {
                return false;
            }
            current = current.children[i];
        }

        // At the end of the iteration it's known the prefix exist
        return true;
    }
}
