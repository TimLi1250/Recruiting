# Websites:
# https://www.interviewcoder.co/blog/scale-ai-software-engineer-interview
# https://www.linkjob.ai/interview-questions/scale-ai-hackerrank-assessment-questions/


# OA is one singular question on Hacker Rank

# 1. Transactional Key-Value Store
# Build an in-memory dictionary that supports reversible changes. The interface is a class rather than a single
# pure function.

'''
We need to implement this interface:
class TransactionalKVStore:
    get(key)
    set(key, value)
    delete(key)
    begin()
    rollback()
    commit()
'''
# Let's do part A first, Basic state. Implement get, set, and delete. A missing key returns None. Deleting a missing key is a
# no-op.

# Part B: Nested transactions. begin() opens a nested transaction. rollback() undoes only changes since the
# most recent unmatched begin(), and returns True; with no open transaction it returns False.

# Part C: Commit. commit() permanently accepts all currently open transactions and closes them; return
# False if none are open. After a commit, rollback() cannot undo that history.
_MISSING = object()

class TransactionalKVStore:
    def __init__(self):
        # A
        self.store = {}
        # B
        self.instructions = []

    def get(self, key):
        # A
        if key in self.store:
            return self.store[key]
        else:
            return None

        # We can probably simplify this actually into return self.store.get(key, None)
    def set(self, key, value):
        # A
        previous = self.store.get(key, _MISSING)
        if self.instructions:

            self.instructions.append({key: previous})

        self.store[key] = value



    def delete(self, key):
        # A
        if key not in self.store:
            return

        previous = self.store.get(key, _MISSING)

        if self.instructions:
            self.instructions.append({key: previous})

        del self.store[key]


    # Opens a nested transaction
    def begin(self):
        # B
        self.instructions.append({})

    def rollback(self):
        # B
        if not self.instructions:
            return False
        current_transaction = self.instructions.pop()
        while self.instructions and current_transaction != {}:
            # We can have key: value, key: None for set and key:value for delete
            for key, value in current_transaction.items():
                # If value == None, we know the item was set for the first time, therefore we can just remove it from the store
                if value == _MISSING:
                    del self.store[key]
                    # Here we can also use pop(key, None) in case the key doesn't exist
                # Else we know that the item must've been either deleted or set, in any case we just need to restore it to the previous case
                else:
                    self.store[key] = value

            current_transaction = self.instructions.pop()
        return True

    def commit(self):
        if self.instructions:
            self.instructions = []
            return True
        return False