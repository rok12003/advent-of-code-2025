# Imports 
from aocd import get_data
import pandas as pd

# Source of package: https://pypi.org/project/advent-of-code-data/

# Change as needed depending on day & directory
raw = get_data(year=2025, day=1)
lines = raw.splitlines()

df = pd.DataFrame(lines, columns=["value"])
df.to_csv("day1_input.csv", index=False)
