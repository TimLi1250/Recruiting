'''
Let's take a look at stacks in python.

So we know stacks can push and pop items, but when should we use them?
1. Handling nested structures
2. Reversing items
3. Substitute for recursion
4. Monotonic stacks

'''
# We can define a simple stack like this:
class Stack:
    stack = []

    # this is basically pushing an item onto the stack
    stack.append(3)
    stack.append(5)
    stack.append(7)
    print(stack)
    # pops the last item off the stack
    stack.pop()
    print(stack)
    # peek at the last item without removing it
    print(stack[-1])


'''
As we mentioned above, one of the most common use cases for stacks is to handle nested stuctures. One example of a problem related to this is the "valid parentheses" problem.
In this problem, we want to check if a string of parentheses is valid. A string is valid if:
1. Every opening parenthesis has a corresponding closing parenthesis.
2. The parentheses are closed in the correct order.
3. The string is empty or contains only valid parentheses.

We can just solve this question by adding everything to the stack, and then popping the PAIR off the stack when we find a matching pair. If we reach the end of the string and the stack is empty, then the string is valid.
(We can also return False right away if we find a closing parenthesis without a matching opening parenthesis)

'''


'''
Now let's look at what happens if we want to solve this: 18 - (7 + ( 2 - 4 ) ).
Every time we encounter a "(" we know we need to evaluate whatever is in between that "(" and ")" first. Therefore, we can push our result onto the stack.
To compute the entire expression, we can just pop the stack. 
'''