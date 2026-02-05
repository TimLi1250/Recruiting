'''
Now let's look at hash maps and sets.

hash maps are basically dictionaries, store unordered key value pairs.
sets is just a collection of unique values.

Let's first look at some methods of a hash map:
'''

my_map = {}
# Adding a key value pair
my_map['key'] = 'value'
# Accessing a value by key TWO methods are depicted below
value = my_map['key']
value = my_map.get('key', 'default_value')  # returns 'default_value' if key not found

my_map.items()  # returns a view of the map's items (key-value pairs)
my_map.keys()   # returns a view of the map's keys
my_map.values() # returns a view of the map's values

my_map.pop('key', 'default_value')  # removes the key and returns its value, or 'default_value' if key not found
my_map.popitem()  # removes and returns the LAST INSERTED (key, value) pair
my_map.clear()  # removes all items from the map

# SORTING IN MAPS
d = {"b": 2, "a": 3, "c": 1}

by_key = dict(sorted(d.items(), key=lambda kv: kv[0]))
# {'a': 3, 'b': 2, 'c': 1}
# if we want to sort by descending order, we can just add reverse=True
by_value = dict(sorted(d.items(), key=lambda kv: kv[1]))
# {'c': 1, 'b': 2, 'a': 3}
# same here




# SPECIAL CASE where we want to initialize a map with a default value for all keys
# In this case below, if 'key' is not present, it will be initialized with 0
key = 'key'
my_map.setdefault(key, 0)
# Now we just include the case where 'key' is already present, for example we can inc
my_map[key] += 1  # increment the value associated with 'key' by 1
'''
We can use a hashmap to do the two-sum problem: Given an array and a target sum, find ANY pair of numbers that add up to the target.

Basically, we can just iterate through the array and for each number, we can check if the complement (target - number) exists in the hashmap.
If it does, we can return the pair. If it doesn't, we can add the number to the hashmap.
This way, we can find the pair in O(n) time complexity

'''

def pair_sum(arr, target):
    hashmap = {}
    pairs = []

    for num in range(len(arr)):
        if target - arr[num] in hashmap:
            pairs.append((arr[num], target - arr[num]))
            return pairs
        else:
            hashmap[arr[num]] = num
    return []


# For a set, we can use it like so:

myset = set()
myset.add("apple")
myset.add("banana")
myset.remove("apple")
print("apple" in myset)


'''
Now let's look at the question, Verify a Sudoku Board. To check if a Sudoku board is valid, we can use a set to keep track of the numbers we have seen in each row, column, and 3x3 subgrid.
We just need to create three groups of sets: one for rows, one for columns, and one for subgrids.
From then on, we can just check if a number is already in the set for that row, column or subgrid.

After this question, we can look at the problem of zero striping.
In this question we want to convert each row and column of a matrix to zero if any element in that row or column is zero.

So the general algorithm is as follows:
1. Identify each cell containing a zero and store its row and column indices in two sets.
Therefore, you will get two sets: zero_rows and zero_cols.
2. Iterate through the matrix again and set the elements to zero if their row or column index is in the respective set.

However, we can optimize this by using the first row and first column of the matrix to store the zero information.
1. Use two flags to indicate if the first row and first column need to be zeroed.
2. Iterate through the matrix (excluding the first row and first column) and for each zero found,
set the corresponding first row and first column elements to zero.
3. Iterate through the matrix again (excluding the first row and first column) and set the elements to zero if their corresponding
first row or first column element is zero.
4. Finally, use the flags to zero out the first row and first column if needed.

This is better because we are only iterating through the matrix a constant number of times and using O(1) additional space.
'''
