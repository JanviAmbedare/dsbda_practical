from collections import defaultdict

def reducer(mapped_data):
    reduced_data = defaultdict(int)
    for key, value in mapped_data:
        reduced_data[key] += value
    return reduced_data
