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

#include <cassert>
#include <string>

using namespace std;

class Node {
public:
    Node* children[26];  // 26 possible children nodes (a-z)
    bool end_of_word;    // True if node represent the end of the word

    Node() {
        end_of_word = false;
        for (int i = 0; i < 26; ++i)
            children[i] = nullptr;
    }
};

class WordDictionary {
private:
    Node* dictionary;  // Root Node

    // Time Complexity: O(word * 26), when '.' appears. Otherwise, O(word).
    // Space Compelxity: O(word), due to recursion stack usage.
    bool dfs(string word, Node* node) {
        Node* current = node;

        for (int i = 0; i < word.size(); i++) {
            char letter = word[i];

            // If the character is '.', it can match any letter:
            //   Recursively search all possible child nodes.
            //   If any recursive call returns True, the word exists.
            if (letter == '.') {
                for (Node* child : current->children) {
                    if (child != nullptr && dfs(word.substr(i + 1), child)) {
                        return true;
                    }
                }
                return false;
            }

            //  Get the index of the character in the alphabet:
            //    If the character does not exist in the trie, return False.
            char key = word[i] - 'a';
            if (current->children[key] == nullptr) {
                return false;
            }

            current = current->children[key];
        }

        return current->end_of_word;
    }

public:
    WordDictionary() {
        dictionary = new Node();
    }

    // Time Complexity: O(word)
    // Space Compelxity: O(1)
    void addWord(string word) {
        Node* current = dictionary;

        for (char letter : word) {
            int i = letter - 'a';

            if (current->children[i] == nullptr) {
                current->children[i] = new Node();
            }

            current = current->children[i];
        }

        current->end_of_word = true;
    }

    bool search(string word) {
        return dfs(word, dictionary);
    }
};

int main() {
    WordDictionary wordDictionary;

    // Add words
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");

    // Word searches
    assert(wordDictionary.search("bad") == true);
    assert(wordDictionary.search("dad") == true);
    assert(wordDictionary.search("mad") == true);
    assert(wordDictionary.search("pad") == false);

    // Wildcard searches
    assert(wordDictionary.search(".ad") == true);
    assert(wordDictionary.search("b..") == true);
    assert(wordDictionary.search("..d") == true);
    assert(wordDictionary.search("...") == true);
    assert(wordDictionary.search("....") == false);

    // Add more words
    wordDictionary.addWord("a");
    wordDictionary.addWord("ab");
    wordDictionary.addWord("ba");
    wordDictionary.addWord("abc");

    // New words searches
    assert(wordDictionary.search("a") == true);
    assert(wordDictionary.search("ab") == true);
    assert(wordDictionary.search("abc") == true);
    assert(wordDictionary.search("abcd") == false);
    assert(wordDictionary.search("a.") == true);
    assert(wordDictionary.search(".") == true);
    assert(wordDictionary.search("..") == true);
    assert(wordDictionary.search("...") == true);
    assert(wordDictionary.search("....") == false);

    // Mixed searches
    assert(wordDictionary.search("a.c") == true);
    assert(wordDictionary.search("..c") == true);
    assert(wordDictionary.search(".b.") == true);
    assert(wordDictionary.search("b.") == true);

    return 0;
}
