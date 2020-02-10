### my_count()

```
def my_count(nums, value):
    """
    Returns number of occurrences of value in nums
    nums: list of integers
    value: integers
    Returns: integer
    Example: my_count([1, 2, 3, 1], 1) retruns 2
    """
```
...
Use an accumulation pattern to calculate the number of occurrences of value in nums
* Initial value of count is zero
* use a for loop with loop variable called **num** to iterate over **nums**
     * use if statement to check num is equal to given value
         * Thus, at each iteration satisfying if condition
         * Increment **count** by 1
return **count**
