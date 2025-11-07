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


def optimized_nested_loops(list1, list2):
    """
    GOOD: Using set intersection
    O(n + m) time complexity
    """
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)


def optimized_file_reading(filename):
    """
    GOOD: Reading all lines at once or using list comprehension
    Minimizes disk I/O operations
    """
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


def optimized_data_filtering(data):
    """
    GOOD: Single pass with chained operations
    List comprehension is more efficient
    """
    return [item * 2 for item in data if item > 0 and item % 2 == 0]


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
    result = []
    data_len = len(data)
    for i in range(data_len - 1):
        result.append(data[i] + data[i + 1])
    return result


def optimized_global_variable_access():
    """
    GOOD: Cache global variable in local variable
    Local variable access is faster
    """
    global GLOBAL_MULTIPLIER
    GLOBAL_MULTIPLIER = 2
    multiplier = GLOBAL_MULTIPLIER  # Cache in local variable
    result = 0
    for i in range(1000):
        result += i * multiplier
    return result


def optimized_exception_handling(data):
    """
    GOOD: Check type before conversion or use str.isdigit()
    Avoid exceptions for control flow
    """
    result = []
    for item in data:
        if isinstance(item, int):
            result.append(item)
        elif isinstance(item, str) and item.isdigit():
            result.append(int(item))
    return result


def optimized_deep_copy(data):
    """
    GOOD: Use shallow copy when appropriate
    Only deep copy when truly needed
    """
    results = []
    for i in range(100):
        # Shallow copy is much faster when deep copy isn't needed
        temp = data.copy()
        temp['counter'] = i
        results.append(temp)
    return results


# Alternative using dictionary comprehension (even more efficient)
def optimized_deep_copy_v2(data):
    """
    BEST: Use dictionary comprehension and update
    """
    return [{**data, 'counter': i} for i in range(100)]


# Global variable for demonstration
GLOBAL_MULTIPLIER = 1


if __name__ == "__main__":
    print("Demonstrating optimized code patterns...")
    
    # String concatenation
    print("\n1. Testing string concatenation...")
    start = time.time()
    result = optimized_string_concatenation(range(10000))
    print(f"Time: {time.time() - start:.4f}s")
    
    # List search
    print("\n2. Testing list search...")
    data = list(range(10000))
    start = time.time()
    optimized_list_search(data, 9999)
    print(f"Time: {time.time() - start:.4f}s")
    
    # Nested loops
    print("\n3. Testing nested loops...")
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    start = time.time()
    result = optimized_nested_loops(list1, list2)
    print(f"Time: {time.time() - start:.4f}s")
    
    print("\nAll optimized patterns demonstrated.")
