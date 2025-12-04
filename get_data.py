# Imports 
from aocd import get_data
import pandas as pd
import sys

# Source of package: https://pypi.org/project/advent-of-code-data/

# Get day from command line argument, default to 1
day = int(sys.argv[1]) if len(sys.argv) > 1 else 1

# Fetch data
raw = get_data(year=2025, day=day)
lines = raw.splitlines()

# Save to CSV
df = pd.DataFrame(lines, columns=["value"])
df.to_csv(f"day{day}/day{day}_input.csv", index=False)

print(f"Data for day {day} saved to day{day}/day{day}_input.csv")