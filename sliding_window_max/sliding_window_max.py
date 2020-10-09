'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from collections import deque

def sliding_window_max(nums, k):
    max_vals = []
    q = deque()
    # remove all elems from a queue
    for i, n in enumerate(nums):
        while len(q) > 0 and n > q[-1]:
            q.pop()
        
        q.append(n)

        # calc the window range
        window_range = i - k + 1

        # as long as our window range == k, add elements to queue
        if window_range >= 0:
            # add the max element (in this case 1st in queue) to max_values list
            max_vals.append(q[0])

            # check if num on the left needs to be evicted
            # if so, take it out of start of queue
            if nums[window_range] == q[0]:
                q.popleft()
                
    return max_vals
    
    max_values = [0 for _ in range(len(nums))]

    for i in range(len(max_values)):
        current_elem
    

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
