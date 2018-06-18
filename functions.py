"""
Skills function assessment.

Please read the instructions first. Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and returns
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.

###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry",
#        "blackberry", or "currant."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a fruit name and a list of fruits. It should
#        return a new list containing the elements of the input list, along with
#        given fruit, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price of $100 or less and $3 for items over $100. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def hometown(town):
    '''Determines if town is hometown. In this case the hometown is Milpitas
    
    >>> hometown('San Jose')
    False

    >>> hometown('Milpitas')
    True

    >>> hometown('milpitas')
    True

    '''

    if town == 'Milpitas' or town == 'milpitas':
        return True
    return False

def full_name(first_name, last_name):
    '''Returns concatenation of first name and last name

    >>> full_name('Jack', 'Jones')
    'Jack Jones'
    '''
    return '{} {}'.format(first_name, last_name)



def greeting(town, first_name, last_name):
    '''"Prints 'Hi, 'full name here', we're from the same place!' if town is hometown, 
        otherwise prints  'Hi 'full name here', I'd like to visit 'town name here'!' 

    >>> greeting('New York', 'Erik', 'Smith')
    Hi Erik Smith, I'd like to visit New York!

    >>> greeting('Milpitas', 'Eva', 'Brown')
    Hi Eva Brown, we're from the same place!


    '''

    fname = full_name(first_name, last_name)
    if hometown(town) is True:
        print('Hi {}, we\'re from the same place!'.format(fname))
    else: 
        print('Hi {}, I\'d like to visit {}!'.format(fname, town))


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """
    berries = 'strawberry, raspberry, blackberry, currant'
    return fruit in berries

    pass


def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """
    if is_berry(fruit): return 0
   
    return 5
    pass


def append_to_list(lst, fruit):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list(['banana', 'apple', 'blackberry'], 'dragonfruit')
    ['banana', 'apple', 'blackberry', 'dragonfruit']

    >>> fruits = ['banana', 'apple', 'blackberry']
    >>> append_to_list(fruits, 'dragonfruit')
    ['banana', 'apple', 'blackberry', 'dragonfruit']
    >>> fruits
    ['banana', 'apple', 'blackberry']

    """
    new_lst = lst[:]
    new_lst.append(fruit)
    return new_lst
    pass


def calculate_price(base_price, st, tax = 0.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """
    if base_price < 0: return None
    
    price_with_tax = base_price + base_price * tax 
    
    if st == 'CA': fee = price_with_tax * 0.03
    elif st == 'PA': fee = 2
    elif st == 'MA':
        if base_price <= 100: fee = 1
        else: fee = 3
    else: return price_with_tax

    total_price = price_with_tax + fee

    return total_price

    pass


###############################################################################

# PART THREE

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

def append_any_number_to_list(lst, *args):
    '''Add any number of agruments into list and returns entire list
    >>> fruits = ['banana', 'apple', 'blackberry']
    >>> a = 'grape'
    >>> b = 'cherry'
    >>> c = 'mango'
    >>> append_any_number_to_list(fruits, a, b, c)
    ['banana', 'apple', 'blackberry', 'grape', 'cherry', 'mango']

    
    >>> fruits = ['banana', 'apple', 'blackberry']
    >>> a = 'melon'
    >>> b = 'pineapple'
    >>> append_any_number_to_list(fruits, a, b)
    ['banana', 'apple', 'blackberry', 'melon', 'pineapple']


    '''

    for arg in args:
        lst.append(arg)
    return lst 
    
def words_tuple(word):
    '''Prints tuple with the original function argument at index 0 and 
    tripled function argument at index 1

    >>> words_tuple("Balloonicorn")
    ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

    '''
    def tripled_word(word):
        tripled_word = word * 3
        return tripled_word
    words_tuple = (word, tripled_word(word))
    return words_tuple    


# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
