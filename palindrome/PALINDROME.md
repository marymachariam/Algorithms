# Palindrome Number

## Problem Description
Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise. An integer is a palindrome when it reads the same forward and backward. 

For example, `121` is a palindrome while `123` is not.

## The Algorithm

The algorithm checks if a number is a palindrome by converting it to text, reversing it, and comparing it to the original input. 

1. **Check for Negative Numbers**: 
   - First, look at the input number. 
   - If the number is negative (less than zero), it can **never** be a palindrome because of the negative sign at the front (e.g., `-121` read backward becomes `121-`). 
   - The code immediately returns `False` for these cases.

2. **Convert and Reverse**: 
   - If the number is positive, convert the integer into a string of text.
   - Reverse the sequence of characters in that text string.
   - Join those reversed characters back together into a single text block and convert it back into a standard integer.

3. **Compare and Decide**:
   - Compare the newly reversed integer with the original input integer.
   - **If they match perfectly**, return `True` because the number reads exactly the same forward and backward.
   - **If they do not match**, return `False`.


## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(D)$, where $D$ is the number of digits in the integer. Converting the number to a string and reversing it requires visiting every single digit exactly once.
- **Space Complexity:** $\mathcal{O}(D)$ auxiliary space. The algorithm creates a temporary string representation of the number in memory to perform the text reversal, which scales with the number of digits.
