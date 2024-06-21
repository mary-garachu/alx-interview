# Making Change

This project provides a function to determine the fewest number of coins needed to meet a given amount total using given coin denominations.

## Function

### makeChange(coins, total)

Determine the fewest number of coins needed to meet a given amount total.

- **Args:**
  - `coins` (list): A list of the values of the coins in your possession.
  - `total` (int): The amount to be made with the coins.

- **Returns:**
  - `int`: The fewest number of coins needed to meet the total. If the total cannot be met by any number of coins you have, return -1.

## Example

```python
from 0-making_change import makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
