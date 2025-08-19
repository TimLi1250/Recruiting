'''
Let's briefly go over bit manipulation.

Because this topic is not that common let's just go over some examples.
'''

'''
1. Hamming Weights of Integers:
The Hamming Weight of a number is the number of set bits in its binary representation. Given an integer n, we just want to return an array where the ith element
is the Hamming Weight of integer i from 0 to n.

Let's look at an example. For the number 25 in base 10, this gets represented as 11001 in base 2. To determine the number of 1s in this, we need to check if the last
digit is 1 by running x & 1 and then right shifting x (this basically means we compare the second to last bit)

'''

def hamming_weights(n):
    return [count_set_bits(x) for x in range(n+1)]

def count_set_bits(x):
    count = 0
    while x > 0:
        count += x & 1
        x >> 1
    return count

# OPTIMIZATION since we are running the same operation numerous times, we can try using dynamic programming.
# We can see the following relation dp[x] = dp[x >> 1] + (x & 1)
# Furthermore, we have a base case of dp[0] = 0 as there are no set bits when n = 0.

'''
2. Lonely Integer: Given an array where each number occurs twice except one of them, find the unique number.

Here we can use the XOR operator. Since we know that a ^ a = 0 and a ^ 0 = a, we can just XOR all the elements together and by commutative and associative properties,
we get the one lonely integer.

3. Swap Odd and Even bits: Given an unsigned 32-bit integer n, return an integer where all of n's even bits are swapped with their adjacent odd bits.

The approach to this question is that to get the even bits of n, we can use a mask that has all even bits set to 1 and all odd bits set to 0.
If we AND this with the original integer, we will get 0s in the odd bits and the even bits will be preserved.
To get the odd bits of n, we can do something similar where we set all odd bits to 1 and even bits to 0 and also AND it with the original integer.

To get our final answer, we shift the even positions to the left once and odd positions to the right once and the OR them. 
'''