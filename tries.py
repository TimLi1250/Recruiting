'''
Let's take a look at tries. They are basically prefix trees

Every TrieNode should have:
1. datastructure to reference its child nodes (usually a hashmap)
2. End of word indicator (usually a boolean or sometimes a string variable)

Runtimes for inserting a word of length k:
Insert in O(k), Search in O(k), Search Prefix in O(k), Delete in O(k)
'''

# We can initialize a TrieNode class like below:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        return node.is_word

    def has_prefix(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        return True

'''
Now let's look at the problem: Insert and Search words with wildcards. For example if we want to search the word "ra." this could be
"rat" or "ran"

Here we need to do something different: When we encounter one of these wildcards, we need to explore all child nodes as the "." may
match any character. We can perform a recursive call for each child node to search the remainder of the word.
In this case, we can define a helper function search_helper(self, word_index: int, word: str, node: TrieNode) -> bool
* the index defines the start of the remaining substring that needs to be searched
* TrieNode (usually the child) where we are starting the search from
'''

'''
Let's take a look at Finding All Word on a Board. In this question, we are given a 2D board of characters and an array of words.
We want to find which of those words can be "drawn" on the board

For each cell on the board that matches one of the root node's children, make a recursive DFS call to that cell passing in the
corresponding node. At each of these DFS calls,

1. Check if the current node represents the end of a word. If it does, add that word to the output
2. Mark the current cell as visited (we can just use '#')
3. Recursively explore all adjacent cells that correspond with a child of the current TrieNode
4. Backtrack by reverting the cell back to its original character (marking it as unvisited)

'''
