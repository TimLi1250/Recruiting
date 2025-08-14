'''
Let's take a look at Intervals

There are three types of intervals:
1. Closed
2. Open
3. Half-open

The main challenge in interval questions is to manage overlapping intervals correctly.
1. One strategy is sorting intervals
We can do this in numerous ways. A common strategy is to sort the intervals by their start point.
We can also separate the start and end points into two different arrays.

'''

'''
Let's take a look at the question: Merging overlapping intervals
The two main challenges to this problem is just
1. Identifying which intervals overlap each other
2. Merging those intervals

If we have two intervals A and B, we see that there is only an overlap if A.end is GREATER THAN OR EQUAL to B.start.
Furthermore, we can see that by sorting these intervals from their starting point,

'''

from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:

    if not intervals:
        return []
    # 1) sort by starting point
    intervals.sort(key=lambda x: x[0])

    # add the first interval in
    merged = []
    cur_start, cur_end = intervals[0]

    # 2) sweep and merge
    for s, e in intervals[1:]:
        if s <= cur_end:               # overlap or touch -> merge
            cur_end = max(cur_end, e)  # extend the current interval
        else:
            # if we encounter a new interval that does not overlap anything before it we add the previous interval to the merged list
            merged.append([cur_start, cur_end])
            cur_start, cur_end = s, e

    merged.append([cur_start, cur_end])
    return merged


'''
Now let's look at the question where we have two sets of intervals and we want to return the overlaps of the intervals.

Here we want to notice that let's say we have an interval A that has a starting point less than the starting point of interval B
1. Check if there even is an overlap. As we stated before, this happens when A.end >= B.start
2. If there is an overlap, we can record this overlap as [B.start, min(A.end, B.end)]

'''

'''
Finally let's look at a slightly harder problem, largest overlap of intervals.
In this question, we are given an array of intervals and we want to determine the maximum amount of intervals that overlap at any point.
Each interval is half-open which means it includes the starting point but exclude the ending point.

Here we can use a sweeping line algorithm where we can convert the list of intervals into a single list of points.
Let's say we have an list of intervals: [[1, 3], [2, 5], [5, 7], [7, 9]]
We can convert this into a single list that also tells whether the index is a starting or ending point.
[1 (S) 2 (S) 3(E) ... ]
Now to run the sweeping line algorithm all we need to do is to iterate through the array and every time we encounter an S, we add 1 to the
overlap counter and every time we encounter a E, we subtract one from the overlap counter.

Finally we need to account for an edge case where let's say we have an interval that starts at 5 and another that ends at 5.
Then, because these are half-open intervals, we need to have the 5 (E) before the 5(S), otherwise we will have a maximum that is one too high.


'''