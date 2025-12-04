# Imports
import pandas as pd

# Loading in data 
df = pd.read_csv("day1_input.csv")

# Starting position of dial & and count.
start = 50
sum = start

# Adding new var -- count
total_count = 0

# Going through each instruction & summing up every instance of when we hit 0.
for rotation in df['value']:

    # Isolating two pieces of information
    direction = rotation[0]
    magnitude = int(rotation[1:])

    # Split into full rotations and partial
    full_rotations = magnitude // 100
    partial = magnitude % 100

    # Adjusting new_sum. This var helps track if we've passed zero.
    if direction == 'R':
        temp_pos = sum + partial
        crossed = 1 if sum != 0 and temp_pos >= 100 else 0
        sum = temp_pos % 100
    else:
        temp_pos = sum - partial
        crossed = 1 if sum != 0 and temp_pos <= 0 else 0
        sum = (100 + temp_pos) % 100

    # Add full rotations + any crossing from partial
    total_count += full_rotations + crossed

# Final output
print(total_count)
