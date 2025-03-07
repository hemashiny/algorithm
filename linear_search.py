# -*- coding: utf-8 -*-
"""linear search.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YKI0SG7KzD8-jwf-_-LYjPnUsnOwyTdl
"""

import time
import random
import matplotlib.pyplot as plt
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
list_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
search_times = []
for size in list_sizes:
    arr = list(range(size))  # Creating a sorted list of given size
    target = random.choice(arr)  # Random target element
    start_time = time.time()
    linear_search(arr, target)
    end_time = time.time()
    elapsed_time = end_time - start_time
    search_times.append(elapsed_time)
plt.plot(list_sizes, search_times, marker='o', linestyle='-', color='b')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Linear Search Time Complexity")
plt.grid(True)
plt.show()