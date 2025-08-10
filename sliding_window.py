'''
Sliding window is a subset of the two-pointer technique.
There are two types of sliding window techniques:
1. Fixed-size sliding window
2. Dynamic-size sliding window

For the dynamic-size sliding window, we usually approach something like this:
1. If the window satifies some condition, expand it until it no longer satisfies the condition.
2. If the window does not satisfy the condition, shrink it until it satisfies the condition again
'''

# A simple example of a fixed-sized sliding window would be substring anagrams.
# Here it is good to use a fixed-size sliding window because the anagram of a word and the word itself have the same length.
# To keep track of the characters in the current window, we can use a dictionary or a list.

'''
Now let's look at the longest substring without repeating characters problem.
Here we can consider a dynamic-size sliding window.

We can use a hashset to keep track of the characters in the current window.
We can then do two things:
1. If the character is not in the hashset, we can add it to the hashset and expand the window.
2. If the character is in the hashset, we can remove characters from the start of the window until the character is no longer in the hashset.

Finally, we just need to keep track of the maximum length of the window we have seen so far.

(We can also perform an optimization, by adding the current character to the hashset, we can shrink the window to the
index to the right of the last occurence of the character)

For example, let's say our hash set currently contains {'a', 'b', 'c'} and we encounter the character 'b'.
We can just shrink the window to the right of the last occurence of 'b', which is the index of 'b' + 1.

'''
def longest_unique_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        # Else if the character is already in the set, we need to shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add the current character to the set
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

'''
Now let's look at the longest uniform substring after replacements.
This question basically asks us to find the longest substring that can be made uniform by replacing at most k characters.

The approach to this question also uses a dynamic-size sliding window.
We can use a hash map to keep track of the frequency of characters in the current window.
We can then do two things:

Based on the condition: (i.e., the number of characters that need to be replaced is less than or equal to k).
The number of characters that need to be replaced is equal to the size of the window minus the frequency of the most common character in the window.

1. If the window satisfies the condition, we can expand the window.
2. If the window does not satisfy the condition, we can SLIDE the window from the left until it satisfies the condition
again.
'''
def longest_uniform_substring(s: str, k: int) -> int:
    char_count = {}
    left = 0
    max_length = 0
    max_freq = 0

    for right in range(len(s)):
        # This checks for the most frequent character in the current window
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_freq = max(max_freq, char_count[s[right]])

        # If the current window size minus the frequency of the most common character is greater than k,
        # we need to SLIDE the window from the left
        while (right - left + 1) - max_freq > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1


    return max_length