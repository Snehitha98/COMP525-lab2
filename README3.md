### my_index()
```
def my_index(sentence, word):
    """
    Returns the lowest index in sentence where word is found, such that word
    is contained within sentence. Returns None if not found.
    sentence: string
    word: string
    Returns: non-negative integer or None
    Example: my_index('bye bye', 'ye') returns 1
    """
```
...

Use an accumulation pattern to return the lowest index in sentence where word is found or returns None if not found.
* initialize **index** with null list
* Define and initialize an accumulator called **length**, of type integer that returns range of number of elements in a sentence
* Initialize **i** with a value of zero
* use a for loop with loop variable called **n** to iterate over **length**
      * use if statement to check sentence is equal to word
           * use if statement to check length of word is greater than one and next letter of sentence is equal to next letter of word
                 * append **n** to **index**, of type list
           * use else statement
                 * append **n** to **index**, of type list
      * use if condition to check word is not in sentence
         * Returns None
   * use a if statement to check if length of index is greater than zero
     * assign first value of a list index to variable index
return **index**
