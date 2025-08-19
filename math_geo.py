'''
This is the last chapter and we are looking at several problems related to math and geometry.

'''

'''
1. Spiral Matrix: How do we traverse a mxn matrix in a spiral order.

To approach this question, we can use boundaries. We can begin by intializing the boundaries as top = 0, bottom = m-1, left = 0, right = n-1.
As we traverse through the matrix in a spiral pattern, we can just update these boundaries.

'''

def spiral_matrix(matrix):
    if not matrix:
        return []
    result = []
    # intialize our boundaries
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1

    while top <= bottom and left <= right:
        # move from left to right along the top boundary
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1
        # move from top to bottom along the right boundary
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1
        # move from right to left along the bottom boundary but before that check if bottom boundary has passed top boundary
        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        # move from bottom to top along the left boundary but before that check if right boundary has passed left boundary
        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

'''
2. Reverse 32-Bit Integer

Let's take a look at how we can reverse a positive integer.
* Extract the last digit through mod 10
* Remove the last digit by // 10
* Append the digit to the reversed integer through n = n * 10 + digit

It turns our that this will also work for negative integers so we just need to look at when will an integer overflow occur.

For integer overflow, we need to check the reversed integer before appending the last digit. We have three cases.
    1. reversed_n < INT_MAX // 10, in this case, multiplying by 10 and adding a digit is safe
    2. reversed_n == INT_MAX // 10, we see that the last digit matters but it won't cause an overflow so we don't need to worry about this case
    3. reversed_n > INT_MAX // 10, overflow is GUARANTEED to happen so we need to return 0 if this is the case

'''

'''
3. Maximum Collinear Points: Given a set of points, determine the maximum number of points that lie along the same straight line.

To approach this question, we know that if two pairs of points are collinear, they must have the same slope. However, just because they have the same slope
does not mean they are collinear. They need to have the same y-intercept. Therefore, how can we guarantee they have the same y-intercept. We take the slope of
all points in regards to a "focal point." Therefore, for every point in the graph we keep a hash map of what slope has the greatest frequency (this will give us
the number of collinear points to that focal point) and take the maximum from there.
'''