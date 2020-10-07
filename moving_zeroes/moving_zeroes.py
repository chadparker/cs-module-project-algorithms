'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # leftNumbers = []
    # rightNumbers = []
    # for num in arr:
    #     if num == 0:
    #         rightNumbers.append(num)
    #     else:
    #         leftNumbers.append(num)
    # return leftNumbers + rightNumbers

    # alternate using list comprehensions:
    leftNumbers = [num for num in arr if num != 0]
    rightNumbers = [num for num in arr if num == 0]
    return leftNumbers + rightNumbers

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")