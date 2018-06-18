
"""List Assessment
Edit the functions until all of the doctests pass when
you run this file.
"""


def print_indices(items):
    """Print each item in the list, followed by its index. Do this without
    using a "counting variable" --- that is, don't do something like this::
        count = 0
        for item in list:
            print(count)
            count = count + 1
    Output should look like this::
        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        Toyota 0
        Jeep 1
        Volvo 2
        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        Toyota 0
        Jeep 1
        Toyota 2
        Volvo 3

    """

    for i in range(len(items)):
        print(items[i], i)
  
    
def words_in_common(words1, words2):
    """Find words in common.
    Given 2 lists of words, return the words that are in common
    between the two, sorted alphabetically.
    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists).
    For example::
        >>> words_in_common(
        ...    ["Python", "Ruby", "R", "C++", "Haskell"],
        ...    ["Lizard", "Turtle", "Python"]
        ...    )
        ['Python']

    The returned list should not have any duplicates::
        >>> words_in_common(
        ...    ["cheese", "bagel", "cake", "cheese"],
        ...    ["hummus", "cheese", "beets", "kale", "bagel", "cake"]
        ... )
        ['bagel', 'cake', 'cheese']

    If there are no words in common, return an empty list::
        >>> words_in_common(
        ... ["lamb", "chili", "cheese"],
        ... ["cake", "ice cream"]
        ... )
        []

    If a duplicate exists in the original lists, the result will
    contain the value only once::
        >>> words_in_common(
        ...    ["Python", "Ruby", "R", "C++", "Haskell"],
        ...    ["Lizard", "Turtle", "Python", "Python"]
        ...    )
        ['Python']
    """
    words1_set = set(words1)
    words2_set = set(words2)
    words_in_common = list(words1_set & words2_set)

    if words_in_common == []:
        return words_in_common

    return sorted(words_in_common)

        


def every_other_item(items):
    """Return every other item in `items`, starting at first item.
    For example::
       >>> every_other_item(['a', 'b', 'c', 'd', 'e', 'f'])
       ['a', 'c', 'e']
       >>> every_other_item(["pickle", "pickle", "juice", "pickle", "juice", "pop"])
       ['pickle', 'juice', 'juice']
       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """
    every_other_item = []
    for i in range(len(items)):
        if i % 2 == 0: every_other_item.append(items[i])
        

    return every_other_item


def smallest_n_items(items, n):
    """Return the `n` smallest integers in list, in descending order.
    You can assume that `n` will be less than the length of the list.
    For example::
    >>> smallest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [42, 6, 2]

    It should work when `n` is 0::
    >>> smallest_n_items([3, 4, 5], 0)
    []

    If there are duplicates in the list, they should be counted
    separately::
    >>> smallest_n_items([3, 1, 3, 2, 1, 1], 2)
    [1, 1]

    """
    items.sort()
    
    smallest_n_items = []
    for i in range(n):
        smallest_n_items.append(items[i])
        
    smallest_n_items.sort(reverse = True)
    
    return smallest_n_items


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")