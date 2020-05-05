import re

def count_words(str):
    """
    >>> count_words("oh what a day what a lovely day")
    {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
    >>> count_words("don't stop believing")
    {"don't": 1, 'stop': 1, 'believing': 1}
    """

    a_dict = {}
    for word in re.findall(r"\b[\w\']+\b", str.lower()):
        a_dict[word] = a_dict.setdefault(word, 0) + 1
        #a_dict[word] = a_dict[word]+1 if word in a_dict else 1
    return a_dict