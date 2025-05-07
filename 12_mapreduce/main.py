# main.py
from mapper import mapper
from reducer import reducer

# Read log file
with open('logs.txt', 'r') as file:
    lines = file.readlines()

# Simulate mapper
mapped = [mapper(line) for line in lines]
mapped = [item for item in mapped if item is not None]

# Shuffle and sort (group by key)
mapped.sort(key=lambda x: x[0])

# Simulate reducer
reduced = reducer(mapped)

# Print result
for key in sorted(reduced):
    print(f"{key}\t{reduced[key]}")
