# hash_distribution.py

import sys
from collections import Counter

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'\u25a0' * count}{padding} ({count})".encode('utf-8').decode(sys.stdout.encoding))
