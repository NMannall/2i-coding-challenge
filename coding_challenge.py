def count_sum_pairs(array, target):
    """
    Looks for pairs of numbers in the provided array which sum to the target.
    Each element can only be used in one pair. The function returns the count
    of how many such pairs it finds.

    It is assumed the array has already been sorted in ascending order. The
    array can contain negative values and the target can be negative.

    :param array: Array of integers sorted in ascending order
    :param target: Integer target value
    :return: Number of pairs that sum to the target
    """

    # All elements in 'array' must be integers, otherwise a ValueError is raised
    if not all(isinstance(item, int) for item in array):
        raise(ValueError, "All elements of the array must be integers.")

    # The 'target' must be an integer, otherwise a ValueError is raised
    if not isinstance(target, int):
        raise(ValueError, "The target must be an integer.")

    pair_count = 0

    length = len(array)
    lower_index = 0
    upper_index = length - 1

    # Move two array pointers towards each other
    # If they meet we have checked all the pairs
    while lower_index < upper_index:
        value = array[lower_index] + array[upper_index]
        if value == target:
            pair_count += 1
            lower_index += 1
            upper_index -= 1
        elif value > target:
            upper_index -= 1
        else:  # value must be less than our target
            lower_index += 1

    return pair_count


if __name__ == '__main__':
    print(count_sum_pairs([3, 4, 5, 6], 1))
    print(count_sum_pairs([0, 15, 32, 2000, 15000], 15))
    print(count_sum_pairs([1, 1, 10, 32, 41], 42))
