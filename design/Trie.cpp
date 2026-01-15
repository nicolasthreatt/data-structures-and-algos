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

#include <cassert>
#include <iostream>
#include <string>

using namespace std;

class TrieNode {
public:
    TrieNode* children[26];  // 26 possible children nodes (a-z)
    bool isEndOfWord;        // True if node represent the end of the word

    TrieNode() {
        isEndOfWord = false;
        for (int i = 0; i < 26; ++i)
            children[i] = nullptr;
    }
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* current = root;

        // Iterate through each character in the word:
        //   Get the index of the character in the alphabet
        //   If the character does not exist in the trie, create a new node
        //   Update the current node to the next node
        for (char letter : word) {
            int i = letter - 'a';
            if (current->children[i] == nullptr) {
                current->children[i] = new TrieNode();
            }
            current = current->children[i];
        }

        // Mark the last node as the end of the word
        current->isEndOfWord = true;
    }

    bool search(string word) {
        TrieNode* current = root;

        // Iterate through each character index in the word:
        //   If the character does not exist in the trie, return False.
        //   If the character exists in the trie, update the current node to the next node.
        for (char letter : word) {
            int i = letter - 'a';
            if (current->children[i] == nullptr) {
                return false;
            }
            current = current->children[i];
        }

        // Mark the last node as the end of the word
        return current->isEndOfWord;
    }

    bool startsWith(string prefix) {
        TrieNode* current = root;

        // Iterate through each character in the prefix:
        //   If the character does not exist in the trie, return False.
        //   If the character exists in the trie, update the current node to the next node.
        for (char letter : prefix) {
            int i = letter - 'a';
            if (current->children[i] == nullptr) {
                return false;
            }
            current = current->children[i];
        }

        // At the end of the iteration it's known the prefix exist
        return true;
    }
};

int main() {
    Trie trie;

    trie.insert("apple");
    assert(trie.search("apple") == true);
    assert(trie.search("app") == false);
    assert(trie.startsWith("app") == true);

    trie.insert("app");
    assert(trie.search("app") == true);

    assert(trie.search("appl") == false);
    assert(trie.startsWith("appl") == true);
    assert(trie.startsWith("apple") == true);
    assert(trie.startsWith("banana") == false);

    trie.insert("banana");
    assert(trie.search("banana") == true);
    assert(trie.search("ban") == false);
    assert(trie.startsWith("ban") == true);

    trie.insert("a");
    assert(trie.search("a") == true);
    assert(trie.startsWith("a") == true);
    assert(trie.search("b") == false);

    return 0;
}
