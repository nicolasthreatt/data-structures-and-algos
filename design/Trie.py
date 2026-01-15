"""
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
"""


class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]  # 26 possible children nodes (a-z)
        self.isEndOfWord = False                   # True if node represents the end of the word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """Inserts a word into the trie.

        Time Comexity: O(n), n is the length of the word.

        Args:
            word: The word to insert into the trie.
        """
        current = self.root

        # Iterate through each character in the word:
        #   Get the index of the character in the alphabet
        #   If the character does not exist in the trie, create a new node
        #   Update the current node to the next node
        for char in word:
            index = ord(char) - ord("a")
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]

        # Mark the last node as the end of the word
        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        """Searches a word in the trie.

        Time Comexity: O(n), n is the length of the word.

        Args:
            word: The word to insert into the trie.

        Returns:
            True if there is a previously inserted string word that has the prefix prefix,
            and false otherwise.
        """
        current = self.root

        # Iterate through each character index in the word:
        #   If the character does not exist in the trie, return False.
        #   If the character exists in the trie, update the current node to the next node.
        for char in word:
            index = ord(char) - ord("a")
            if not current.children[index]:
                return False
            current = current.children[index]

        # At the end of the iteration, check if the current node is the end of the word.
        return current.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """Check if the prefix is in the trie.

        Time Complexity: O(n), n is the length of the prefix.

        Args:
            prefix: The prefix to check if it is in the trie.

        Returns:
            True if the string word is in the trie (i.e., was inserted before),
            and false otherwise.
        """
        current = self.root

        # Iterate through each character in the prefix.
        #   If the character does not exist in the trie, return False.
        #   If the character exists in the trie, update the current node to the next node.
        for char in prefix:
            index = ord(char) - ord("a")
            if not current.children[index]:
                return False
            current = current.children[index]

        # At the end of the iteration it's known the prefix exist
        return True


if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True

    trie.insert("app")
    assert trie.search("app") is True

    assert trie.search("appl") is False
    assert trie.startsWith("appl") is True
    assert trie.startsWith("apple") is True
    assert trie.startsWith("banana") is False

    trie.insert("banana")
    assert trie.search("banana") is True
    assert trie.search("ban") is False
    assert trie.startsWith("ban") is True

    trie.insert("a")
    assert trie.search("a") is True
    assert trie.startsWith("a") is True
    assert trie.search("b") is False
