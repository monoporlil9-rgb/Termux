#!/usr/bin/env python3
"""
Optimized versions of the inefficient code patterns
This file demonstrates best practices for performance optimization
"""

import time


def optimized_string_concatenation(items):
    """
    GOOD: Using join() for string concatenation
    join() is O(n) complexity - much more efficient
    """
    return ",".join(str(item) for item in items)


def optimized_list_search(data, target):
    """
    GOOD: Using set for membership checks
    Set lookup is O(1) average case
    """
    return target in set(data)


def optimized_nested_loops(first_list, second_list):
    """
    GOOD: Using set intersection
    O(n + m) time complexity
    """
    first_set = set(first_list)
    second_set = set(second_list)
    return list(first_set & second_set)


def optimized_file_reading(filename):
    """
    GOOD: Reading all lines at once or using list comprehension
    Minimizes disk I/O operations
    """
    with open(filename, 'r') as file_handle:
        return [current_line.strip() for current_line in file_handle]


def optimized_data_filtering(data):
    """
    GOOD: Single pass with chained operations
    List comprehension is more efficient
    """
    return [number * 2 for number in data if number > 0 and number % 2 == 0]


def optimized_dictionary_iteration(data_dict):
    """
    GOOD: Using values() directly or items()
    Avoids redundant key lookups
    """
    return sum(data_dict.values())


def optimized_function_calls_in_loop(data):
    """
    GOOD: Store length in a variable outside the loop
    Avoid repeated function calls
    """
    pairwise_sums = []
    data_length = len(data)
    for index in range(data_length - 1):
        pairwise_sums.append(data[index] + data[index + 1])
    return pairwise_sums


def optimized_global_variable_access():
    """
    GOOD: Cache global variable in local variable
    Local variable access is faster
    """
    global GLOBAL_MULTIPLIER
    GLOBAL_MULTIPLIER = 2
    cached_multiplier = GLOBAL_MULTIPLIER  # Cache in local variable
    accumulated_sum = 0
    for counter in range(1000):
        accumulated_sum += counter * cached_multiplier
    return accumulated_sum


def optimized_exception_handling(data):
    """
    GOOD: Check type before conversion or use str.isdigit()
    Avoid exceptions for control flow
    """
    converted_integers = []
    for data_element in data:
        if isinstance(data_element, int):
            converted_integers.append(data_element)
        elif isinstance(data_element, str) and data_element.isdigit():
            converted_integers.append(int(data_element))
    return converted_integers


def optimized_deep_copy(data):
    """
    GOOD: Use shallow copy when appropriate
    Only deep copy when truly needed
    """
    modified_dicts = []
    for iteration_count in range(100):
        # Shallow copy is much faster when deep copy isn't needed
        copied_dict = data.copy()
        copied_dict['counter'] = iteration_count
        modified_dicts.append(copied_dict)
    return modified_dicts


# Alternative using dictionary comprehension (even more efficient)
def optimized_deep_copy_v2(data):
    """
    BEST: Use dictionary comprehension and update
    """
    return [{**data, 'counter': iteration_count} for iteration_count in range(100)]


# Global variable for demonstration
GLOBAL_MULTIPLIER = 1


if __name__ == "__main__":
    print("Demonstrating optimized code patterns...")
    
    # String concatenation
    print("\n1. Testing string concatenation...")
    start_time = time.time()
    concatenation_result = optimized_string_concatenation(range(10000))
    print(f"Time: {time.time() - start_time:.4f}s")
    
    # List search
    print("\n2. Testing list search...")
    search_data = list(range(10000))
    start_time = time.time()
    optimized_list_search(search_data, 9999)
    print(f"Time: {time.time() - start_time:.4f}s")
    
    # Nested loops
    print("\n3. Testing nested loops...")
    first_number_list = list(range(1000))
    second_number_list = list(range(500, 1500))
    start_time = time.time()
    common_result = optimized_nested_loops(first_number_list, second_number_list)
    print(f"Time: {time.time() - start_time:.4f}s")
    
    print("\nAll optimized patterns demonstrated.")
