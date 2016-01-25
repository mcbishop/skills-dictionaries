"""Skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list:

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers:

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]



    """
#previously: return set[words]
    rose_dict = {}
    for word in words:
        if word in rose_dict.keys():
            rose_dict[word] += 1
        else:
            rose_dict[word] = 1
    return rose_dict.keys()

#also:
    # rose_dict = {}
    # for word in words:
    #     rose_dict[word] = 1
    # return rose_dict.keys()

def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([4, 3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are different data types.

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]

    """

 # previously:   return set(list1) & (set(list2))
 

    dict_1 = {}
    dict_2 = {}

    #put each key from list1 in a dictionary with value of 1. If you find the same value again, overwrite. This way dict1 is already unique.
    for item in list1:
        dict_1[item] = 1
    #Same for list2. Now you have two dictionarys with unique keys.
    for item in list2:
        dict_2[item] = 1

    #a 3rd way. THIS WORKED BUT USED IF - IN - NOT ALLOWED!
    # for key in dict_1.keys():
    #     if key in dict_2.keys():
    #         dict_3[key] = 1
    # return dict_3.keys()

    #make a list of each set ofkeys, and return only those keys shared between lists.
    list3 = (dict_1.keys())
    list4 = (dict_2.keys())
    return set(list3) & set(list4)


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    unique_dict = {}
    input_string = input_string.split(" ")
    for word in input_string:
        if word not in unique_dict:
            unique_dict[word] = 0
        unique_dict[word] += 1

    return unique_dict


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

   English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be

    For example:

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    pirate_dict={
        "sir":         "matey",
        "hotel":       "fleabag inn",
        "student":     "swabbie",
        "boy":         "matey",
        "professor":   "foul blaggart",
        "restaurant":  "galley",
        "your":        "yer",
        "excuse":      "arr",
        "students":    "swabbies",
        "are":         "be",
        "restroom":    "head",
        "my":          "me",
        "is":         "be",
        "man":        "matey",
        }


#revise so that it translates words more quickly
    phrase = phrase.split(' ')
    new_phrase = []
#    new_string = ''
    for word in phrase:
        if word in pirate_dict:
            new_phrase.append(pirate_dict[word])
        else:
            new_phrase.append(word)
    #iterate through each item in new_phrase, and return it in one string, separated by ' '
    return ' '.join(new_phrase)

    #previously:
    # for word in new_phrase:
    #     if word == new_phrase[0]:
    #         new_string = word
    #     else:
    #         new_string = new_string + ' ' + word

    # return new_string



def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items---the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
   #try using a dictionary to solve this one.
    
    words_dict = {}

    for word in words:
        if (len(word)) not in words_dict.keys():
            words_dict[len(word)] = [word]
        else:     
            words_dict[len(word)] += [word]

    return words_dict.items()

#    new_tuples = ( sorted(words_dict.values())

    # word_list = []
    # for word in words:  #for each word in the set of words
    #     #if word count matches the first item in tuple, add word to list
    #     if word_list: #if word_list contains something
    #         found_match = False
    #         for item in word_list: #for each set of tuples in word_list
    #             current_tuple = item
    #             if item[0]==len(word): #if item matches length of word
    #                 found_match = True
    #                 item[1].append(word) #if item matches length of word, append list to add word.
    #         if not found_match:
    #             word_list.append((len(word),[word]))
    #     else:
    #         word_list.append((len(word),[word]))
    # return sorted(word_list)

def get_sum_zero_pairs(input_list):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    #try using a dictionary to do this.
    from math import fabs 

    zero_dict = {}
    for num1 in input_list:  #go through every number in the list
        for num2 in input_list:  #compare it to...every number in the list, including itself
            if num1 + num2 == 0:  #does the sum equal zero?
                if fabs(num1) not in zero_dict.keys():  #verify unique dictionary entry
                    zero_dict[num1] = [num1,num2]  #add unique dictionary entry!
    return zero_dict.values()


    # previously:  
    # zero_list = []
    # unique_list = list(set(input_list))
    # for num1 in unique_list:
    #     for num2 in unique_list:
    #         if num1+num2 == 0:
    #             zero_list.append([num1,num2])
    #         if num1 == 0:
    #             zero_list.append([num1,num1])

    # for (num1,num2) in zero_list:
    #     for (num3, num4) in zero_list:
    #         if (num1 == num4) and (num2 == num3):
    #             zero_list.remove([num3,num4])


    # return zero_list


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
