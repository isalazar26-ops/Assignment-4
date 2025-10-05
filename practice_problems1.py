"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()
    for pid in product_ids: 
        if pid in seen:
            return True
        seen.add(pid) 
    return False
    pass


# Justification: A set is ideal because it automatically 
# prevents duplicates and allows 0(1) average-time lookups.
#  Each insertion/check is efficient, so the whole algorithm 
# runs in 0(n) time with 0(n) space in the worst case. 


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()
        pass

    def add_task(self, task):
        self.queue.append(task)
        pass

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.popleft()
        return None 
        pass


# Justication: A queue structure is the natural fit for FIFO 
# (first-in-first-out) task management. Both append (enqueue) 
# and popleft (dequeue)are 0(1), making this highly efficient 
# for repeated operations.


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.unique_value = set()
        pass

    def add(self, value):
        self.unique_values.add(value)
        pass

    def get_unique_count(self):
        return len(self.unique_values)
        pass


#Justification: A set is best for tracking unique values, 
# since duplicate are automatically ignored. Insertions 
# are 0(1) on average, and getting the number of unique 
# items is 0(1) by calling len().
