"""
lab2.py
Mihaela Sabin
Creaated February 4, 2020
Practice with sequence traversal and string processing
"""


def my_len(word):
    """
    Returns the word length.
    Implemenation requirement: use the accumulation pattern, NOT len()
    word: string
    Returns: Integer value corresponding to length of word

    Example: my_len('abc') returns 3
    """


def my_find(word, letter):
    """
    Tests if letter is in word. Use the accumulation pattern, NOT str find()
    word: string
    letter: one-character string
    Returns: True if letter is in word, False otherwise

    Example:
        my_find('dog', 'o') returns True
    """


def my_count(nums, value):
    """
    Returns number of occurrences of value in nums
    nums: list of integers
    value: integers
    Returns: integer
    Example: my_count([1, 2, 3, 1], 1) retruns 2
    """


def my_index(sentence, word):
    """
    Returns the lowest index in sentence where word is found, such that word
    is contained within sentence. Returns None if not found.
    sentence: string
    word: string
    Returns: non-negative integer or None
    Example: my_index('bye bye', 'ye') returns 1
    """


if __name__ == '__main__':
    # Testing my_len()
    test_case = 'abc'
    expected_result = my_len(test_case)
    print(f'my_len("{test_case}") returns {expected_result}')
