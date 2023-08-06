# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 8/6/2023
# Description: This program defines the bubble sort and insertion sort functions, decorates them
# with the sort_timer decorator then compares the sorting times for lists of various lengths
# using the compare_sorts function. It generates a graph to visualize the comparison of the
# sorting algorithms.

import time
import random
import matplotlib.pyplot as plt
from functools import wraps

def sort_timer(func):
    """
    Decorator function to time how long a function takes to run
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        This function returns the elapsed time
        """
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return elapsed_time
    return wrapper

@sort_timer
def bubble_sort(a_list):
    """
    Defines the bubble sort function and decorates it with the sort_timer decorator
    """
    n = len(a_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list

@sort_timer
def insertion_sort(a_list):
    """
    Defines the insertion sort function and decorates it with the sort_timer decorator
    """
    for i in range(1, len(a_list)):
        key = a_list[i]
        j = i - 1
        while j >= 0 and key < a_list[j]:
            a_list[j + 1] = a_list[j]
            j -= 1
        a_list[j + 1] = key
    return a_list

def make_lists_of_sort_times(sort_func1, sort_func2, lengths):
    """
    Function to generate lists of sort times for each algorithm
    """
    times_func1 = []
    times_func2 = []

    for length in lengths:
        # Generate a random list of length 'length'
        random_list = [random.randint(1, 10000) for _ in range(length)]

        # Create separate copies of the random list
        list_copy1 = random_list.copy()
        list_copy2 = random_list.copy()

        # Time the first sort function
        time_func1 = sort_func1(list_copy1)
        times_func1.append(time_func1)

        # Time the second sort function
        time_func2 = sort_func2(list_copy2)
        times_func2.append(time_func2)

    return times_func1, times_func2

def compare_sorts(sort_func1, sort_func2):
    """
    Function to compare sort algorithms and generate a graph
    """
    lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    times_func1, times_func2 = make_lists_of_sort_times(sort_func1, sort_func2, lengths)

    # Create a graph to compare the times
    plt.plot(lengths, times_func1, label="Bubble Sort")
    plt.plot(lengths, times_func2, label="Insertion Sort")
    plt.xlabel('List Length')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Sort Algorithms')
    plt.legend()
    plt.show()

# Call the compare_sorts function with bubble_sort and insertion_sort
compare_sorts(bubble_sort, insertion_sort)