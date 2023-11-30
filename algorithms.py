
def add_numbers(numbers):
    """
    Ex. add_numbers([9, 5, 11, 6, 1, 15]) returns 47
    :param numbers: a list of numbers
    :return: the sum of all the numbers in the list
    """
    result = []
    for num in numbers:
        sum = 0
        list_length = len(numbers)
        for x in range(list_length):
            sum += numbers[x]
    return sum
numbers = [34,12,7,9]
print(add_numbers(numbers))


def get_max(numbers):
    """
    Ex. get_max([45, 23, 99, 34, 67, 98, 0]) returns 99
    :param numbers: a list of numbers
    :return: The largest number in the list
    """
    max_ = numbers[0]
    length_list = len(numbers)
    for x in range(length_list):
        if numbers[x] > max_:
            max_ = numbers[x]
    return max_
numbers = [17,3245,65,72,45]
result = get_max(numbers)
print(result)

def get_min(numbers):
    """
    Ex. get_min([45, 23, 99, 34, 67, 98, 0]) returns 0
    :param numbers: a list of numbers
    :return: The smallest number in the list
    """
    pass # remove this line when starting your function


def merge(list1, list2):
    """
    Ex. merge([3, 4, 7, 9], [1, 5, 8, 11]) return [1, 3, 4, 5, 7, 8, 9, 11]
    :param list1: a list in sorted order
    :param list2: a second list in sorted order
    :return: a single list consisting of both smaller lists combined in sorted order.
    """
    pass # remove this line when starting your function