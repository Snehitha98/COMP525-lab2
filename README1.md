### my_find()
```
def my_find(word, letter):
    """
    Tests if letter is in word. Use the accumulation pattern, NOT str find()
    word: string
    letter: one-character string
    Returns: True if letter is in word, False otherwise

    Example:
        my_find('dog', 'o') returns True
    """
```
...
Use an accumulation pattern to find if letter is in word
* Define and initialize an accumulator called **length**, of type integer that returns range of number of elements in a word

* use a for loop with loop variable called **k** to iterate over **length**
     * The purpose of the accumulator is to check whether letter is in word at each pass through for loop
     * use a if statement to check whether letter is in word
          * Assigning **True** to result
          * Breaks the loop and goes to return statement
     * use a else statement
          * Assigning **False** to result  

return **result**
