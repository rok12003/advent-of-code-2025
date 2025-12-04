# Imports
import pandas as pd

# Loading in data 
df = pd.read_csv("day1_input.csv")

# Starting position of dial, number of times we've reached 0, and count.
start = 50
count_zero = 0
sum = start

# Going through each instruction & summing up every instance of when we hit 0.
for rotation in df['value']:

    # Isolating two pieces of information
    direction = rotation[0]
    magnitude = int(rotation[1:])
    
    # Adjusting sum
    if direction == 'R':
        sum += magnitude
    else:
        sum -= magnitude

    # Wrapping around the dial
    sum = sum % 100

    # Actual count
    if sum == 0:
        count_zero += 1

# Final output
print(count_zero)
