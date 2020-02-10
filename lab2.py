"""
lab2.py
Mihaela Sabin
Created February 4, 2020
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
    length=0
    for char in word:
        length=length+1
    return length

def my_find(word, letter):
    """
    Tests if letter is in word. Use the accumulation pattern, NOT str find()
    word: string
    letter: one-character string
    Returns: True if letter is in word, False otherwise

    Example:
        my_find('dog', 'o') returns True
    """
    length=range(len(word))
    for k in length:
      if letter == word[k]:
        result="True"
        break
      else:
        result="False"
    return result

def my_count(nums, value):
    """
    Returns number of occurrences of value in nums
    nums: list of integers
    value: integers
    Returns: integer
    Example: my_count([1, 2, 3, 1], 1) returns 2
    """
    count=0
    for num in nums:
        if num == value:
            count+=1
    return count

def my_index(sentence, word):
    """
    Returns the lowest index in sentence where word is found, such that word
    is contained within sentence. Returns None if not found.
    sentence: string
    word: string
    Returns: non-negative integer or None
    Example: my_index('bye bye', 'ye') returns 1
    """
    index = []
    length=range(len(sentence))
    i=0
    for n in length:
        if sentence[n]==word[i]:
            if len(word)>1 and sentence[n+1] == word[i+1]:
                index.append(n)
            else:
                index.append(n)
        if word not in sentence:
          return None

    if(len(index)>0):
        index=index[0]
    return index

if __name__ == '__main__':
    # Testing my_len()
    word = 'abc'
    expected_result = my_len(word)
    print(f'my_len("{word}") returns {expected_result}')
    # test_case1_for_my_len()
    word = 'snehitha loves dance'
    expected_result = my_len(word)
    print(f'my_len("{word}") returns {expected_result}')
    # test_case2_for_my_len()
    word = '  '
    expected_result = my_len(word)
    print(f'my_len("{word}") returns {expected_result}')


    # Testing my_find()
    word = 'dog'
    letter='o'
    expected_result = my_find(word,letter)
    print(f'my_find("{word}",{letter}) returns {expected_result}')
    # test_case1_for_my_find()
    word = 'snehitha'
    letter='g'
    expected_result = my_find(word,letter)
    print(f'my_find("{word}",{letter}) returns {expected_result}')
    # test_case2_for_my_find()
    word = 'data structures'
    letter=' '
    expected_result = my_find(word,letter)
    print(f'my_find("{word}",{letter}) returns {expected_result}')


    # Testing my_count()
    nums = [1, 2, 3, 1]
    value = 1
    expected_result = my_count(nums,value)
    print(f'my_count({nums},{value}) returns {expected_result}')

    # Testing my_index()
    sentence="bye bye"
    word="ye"
    expected_result = my_index(sentence, word)
    print(f'my_index("{sentence}",{word}) returns {expected_result}')
