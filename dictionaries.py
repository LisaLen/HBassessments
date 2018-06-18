"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    words_count_dict = {}

    words = phrase.split()
    for word in words:
        words_count_dict[word] = words_count_dict.get(word, 0) + 1


    return words_count_dict


def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

    Honeydew 2.50
    Cantaloupe 2.50
    Watermelon 2.95
    Musk 3.25
    Crenshaw 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If there are no melons at that price print "None found"

        >>> print_melon_at_price(2.50)
        Cantaloupe
        Honeydew

        >>> print_melon_at_price(2.95)
        Watermelon

        >>> print_melon_at_price(5.50)
        None found
    """
    melons = {'Honeydew': 2.50,
                   'Cantaloupe': 2.50,
                   'Watermelon': 2.95,
                   'Musk':  3.25,
                   'Crenshaw': 3.25,
                   'Christmas': 14.25}

    melons_at_price = []

    for melon in melons:
        if melons[melon] == price:
            melons_at_price.append(melon)

    if melons_at_price == []:
        print('None found')
    else:
        melons_at_price.sort()
        [print(melon_at_price) for melon_at_price in melons_at_price]
    

           



def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    transl_table = {'sir': 'matey',
                    'hotel': 'fleabag inn',
                    'student': 'swabbie',
                    'man': 'matey',
                    'professor': 'foul blaggart',
                    'restaurant': 'galley',
                    'your': 'yer',
                    'excuse': 'arr',
                    'students': 'swabbies',
                    'are': 'be',
                    'restroom': 'head',
                    'my': 'me',
                    'is': 'be'}
    words = phrase.split()
    pirate_phrase = []

    for word in words:
        if word in transl_table:
            pirate_phrase.extend(transl_table[word] + ' ')
        else: 
            pirate_phrase.extend(word + ' ')

    return ''.join(pirate_phrase).rstrip(' ')


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
   
   
    def build_names_chain(names):
        chains = {}
        for name in names:
            search_lst = names[:]
            search_lst.remove(name)
            chains[name] = []
            for search in search_lst:
                if search[0] == name[-1]:
                    chains[name].append(search)          
        return chains

    start_word = names[0]
    
    used_names_set = {start_word}
    result = [start_word]
    chains = build_names_chain(names)
    lst_search = chains[start_word]

    
    while True and lst_search != []:
        for word in lst_search:
            if word not in used_names_set:
                new_word = word
                used_names_set.add(word)
                flag = True               
                break
            else: 
                flag = False
        if flag:
            result.append(new_word)
            lst_search = chains[word]
        else: 
            break

    return result

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print("{" + ", ".join(
            "'{}': {}".format(k, d[k]) for k in sorted(d)) + "}")
    else:
        print(d)

if __name__ == "__main__":
    print()
    import doctest
    if doctest.testmod().failed == 0:
        print("*** ALL TESTS PASSED ***")
    print()
