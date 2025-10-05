"""
Timed Challenge Problem: 


1. Rotate Right
Rotate the values in a collection to the right by k steps.


Example:
Input: [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
"""


from collections import deque

def rotate_right(nums, k):
    if not nums or k <= 0:
        return nums 
    

    dq = deque(nums)
    dq.rotate(k)
    return list(dq)

print(rotate_right([1, 2, 3, 4, 5], 2))
print(rotate_right([1,2], 5))
print(rotate_right([], 3))
print(rotate_right([10], 10))



"""
Timed Challenge Problem: 


3. Remove Duplicates (Keep Order)
Return the values in the order they first appeared, without duplicates.

Example:
Input: ["apple", "banana", "apple", "kiwi", "banana"]
Output: ["apple", "banana", "kiwi"]
"""

def running_total_with_reset(values):
    result = []
    current_total = 0

    for v in values:
        if v < 0:
            current_total = 0
        else:
            current_total += v
        result.append(current_total)

    return result 

print(running_total_with_reset([5, 7, -1, 3, 2]))
print(running_total_with_reset([]))
print(running_total_with_reset([-1, -5, 10]))
print(running_total_with_reset([2, 2, 2]))



"""
Timed Challenge Problem: 

4. Remove Every k-th Value
Remove every k-th value from a collection and return the result.

Example:
Input: [10, 20, 30, 40, 50, 60], k = 3
Output: [10, 20, 40, 50]
"""

def remove_every_ktch(values, k):
    if not values or k <=0:
        return alues 
    
    result = []
    for i, val in enumerate(values, start=1):
        if i % k != 0:
            result.append(val)
    return result 


print(remove_every_ktch([10, 20, 30, 40, 50, 60], 3))
print(remove_every_ktch([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(remove_every_ktch([], 3))
print(remove_every_ktch([100, 200], 5))
print(remove_every_ktch([5, 10, 15], 1))
