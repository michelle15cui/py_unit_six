
def create_list(starting, ending):
    """
    Ex. create_list(4, 10) would return [4, 5, 6, 7, 8, 9, 10]
    :param starting: an integer number
    :param ending: A number greater than the starting number
    :return: list of numbers starting with the first number and going up to and including the second number
    """

    some = list(range(starting, ending+1))
    print(some)

create_list(4, 10)




def find_odds(numbers):
    """
    Ex. find_odds([13, 2, 9, 14, 16, 18, 9, 11, 21]) would return [13, 9, 9, 11, 21]
    :param numbers: a list of numbers
    :return: a new list consisting of only the odd numbers from the original list
    """
    list_one = []
    num = len(numbers)
    print("Length = ", num)
    for x in range(num):
        if numbers % 2 == 1 :
            list_one.append(numbers[x])
    return list_one

numbers = [13, 2, 9, 14, 16, 18, 9, 11, 21]
print("Starting list is: ", numbers)
print("Find odds output: ")
print(find_odds(numbers))
print()


def remove_duplicates(numbers):
    """
    Ex. remove_duplicates([1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7])  would return  [1, 2, 3, 4, 5, 6, 7]
    remove_duplicates9[‘apple’, ‘banana’, ‘banana’, ‘cherry’]) would return [‘apple’, ‘banana’, ‘cherry’]
    :param numbers:
    :return:
    """

    pass # remove this line when starting your function
