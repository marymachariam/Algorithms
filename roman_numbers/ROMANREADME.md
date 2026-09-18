# Roman to Integer Algorithm

## Core Logic
Roman numerals are read from left to right. Usually, values are added together. However, when a smaller numeral appears **before** a larger numeral, it signifies a subtraction pair (e.g., `IV` represents \(5 - 1 = 4\)). 

To handle this, the algorithm evaluates each character by looking ahead to its immediate neighbor on the right.

## Step-by-Step Algorithm

1. **Create a Reference Map**: Set up a lookup table mapping each of the 7 Roman numeral characters (`I`, `V`, `X`, `L`, `C`, `D`, `M`) to its corresponding numerical integer value.
2. **Initialize Running Total**: Create a tracker variable initialized to `0` to hold the cumulative integer sum.
3. **Iterate Through the Text**: Read the input string from left to right, processing one character at a time.
4. **Evaluate the Neighbor**: At each character position, peek at the symbol immediately to its right (if one exists).
5. **Apply Numerical Rules**:
   - **Subtraction Rule**: If the current symbol's value is **strictly less than** the next symbol's value, subtract the current value from the running total.
   - **Addition Rule**: If the current symbol's value is **greater than or equal to** the next symbol's value (or if it is the very last character in the string), add its value to the running total.
6. **Output the Result**: Once all characters have been processed, return the final calculated running total.


## Complexity Analysis
- **Time Complexity:** {O}(N), where \(N\) is the length of the Roman numeral string. The algorithm passes through the string exactly once, executing a constant-time {O}(1) map lookup and comparison step for each character.
- **Space Complexity:** \{O}(1) auxiliary space. The lookup reference map always holds a fixed set of 7 elements regardless of input size, requiring no scalable runtime memory.
