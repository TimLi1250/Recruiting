'''
Let's take a look at Greedy Algorithms

Greedy Algorithms follow the greedy choice property that state the best overall solution can be arrived by making the best possible
decision at each step.

'''

'''
1. Jump to the End: Starting at index 0, you are given an array where each index in the array represents the maximum jump distance from the
current index. Determine if it is possible to reach the end of the array.

To approach this question, we need to recognize that if we can reach the destination from any earlier index, that earlier index becomes
the new destination. Now how do we determine this earlier index?

We want to choose the earliest index from the right. Why? Let's say indices 2, 3 and 5 can all reach the destination. We want to choose
index 5 because all other indices that can reach the final destination can also reach index 5. Therefore we can just look at what can
reach index 5 and then we KNOW for a fact that index 5 can reach the destination.
'''
def jump_to_the_end(nums) -> bool:
    destination = len(nums)-1
    # greedily traverse the array in reverse order to see the earliest index that can reach the destination
    for i in range(len(nums)-1, -1, -1):

        if i + nums[i] >= destination:
            destination = i

    return destination == 0

'''
2. Gas Stations: circular route that contains gas stations. At each station, you can fill your car with a certain amount of gas,
and moving from that station to the next one consumes some fuel.

To approach this question we first need to realize that if the total gas is < total cost, then we don't have enough gas to make it
around the circle. Now let's consider the net gas which can be calculated by the gas - cost. Here we need to realize one thing.
If we can't make it from station a to station b, we can't make it to station b from any of the stations [a, b].

Therefore our job is to find the first spot where we can proceed to the end of the array without running out of gas.
For example, let's say we have the array [1, 1, -3, 2, 1, -4, 3, 1]. We see that at index 2 and 5, we run into negative numbers
when calculating the cumulative sum so we can't continue. Therefore, we can only start at index 6 and that results in us proceeding
to the end of the array
'''

def gas_stations(gas, cost) -> int:
    # If the total gas is less than total cost, then we can't complete the circuit
    if sum(gas) < sum(cost):
        return -1
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        # check if the tank has negative gas, if so we break and continue
        if tank < 0:
            start, tank = i+1, 0
    return start

'''
3. Candies. Children in an array with different ratings. Each child must receive one candy and if two children sit next to each other,
the child with the higher rating must receive more candies.

Here we can use a greedy approach. We know to first give each child one candy. Then from there, we can use two passes. One to handle
that children with a higher rating than their left-side neighbor get more candy and one to handle that children with a higher rating than their
right-side neighbor get more candy. We know this solution works because after the two passes, we have compared both neighbors to the child.

'''

def candies(ratings) -> int:
    n = len(ratings)

    candies = [1] * n
    # first pass, compare child and left-side neighbor
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            # if current child already has more than right side neighbor just keep that amount
            candies[i] = max(candies[i], candies[i+1]+1)
    return sum(candies)