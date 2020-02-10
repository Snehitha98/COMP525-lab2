### my_len()
```
def my_len(word):
    """
    Returns the word length.
    Implemenation requirement: use the accumulation pattern, NOT len()
    word: string
    Returns: Integer value corresponding to length of word

    Example: my_len('abc') returns 3
    """
```
...
Use an accumulation pattern to calculate the length of word
* Define and initialize an accumulator called **length**, of type integer
     * Initial value of length is zero
* use a for loop with loop variable called **char** to iterate over **word**
     * The purpose of the accumulator is to get incremented at each pass through for loop
     * Thus, at each iteration
          * Increment **length** by 1
return **length** 
