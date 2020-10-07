'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    log = {}

    for num in arr:
        if num in log:
            log[num] += 1
            if log[num] == 2:
                # seen twice, not it
                del log[num]
        else:
            log[num] = 1

    if len(log) > 1:
        print("List contains more than one single-number")
        raise Exception

    # return remaining single key
    return next(iter(log))


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")