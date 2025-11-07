#!/usr/bin/env python3
"""
Examples of slow and inefficient code patterns
This file contains common performance anti-patterns that should be avoided
"""

import time
import copy


def inefficient_string_concatenation(items):
    """
    BAD: Using += for string concatenation in a loop
    This creates a new string object on each iteration - O(n^2) complexity
    """
    result = ""
    for item in items:
        result += str(item) + ","
    return result


def inefficient_list_search(data, target):
    """
    BAD: Using list for frequent membership checks
    List lookup is O(n) for each check
    """
    seen = []
    for item in data:
        if item not in seen:
            seen.append(item)
        if item == target:
            return True
    return False


def inefficient_nested_loops(list1, list2):
    """
    BAD: Nested loops for finding common elements
    O(n*m) time complexity
    """
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in common:
                common.append(item1)
    return common


def inefficient_file_reading(filename):
    """
    BAD: Reading file line by line with repeated disk I/O
    """
    lines = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            lines.append(line.strip())
            line = f.readline()
    return lines


def inefficient_data_filtering(data):
    """
    BAD: Multiple passes over the data
    Each filter creates a new list
    """
    result = []
    for item in data:
        if item > 0:
            result.append(item)
    
    result2 = []
    for item in result:
        if item % 2 == 0:
            result2.append(item)
    
    result3 = []
    for item in result2:
        result3.append(item * 2)
    
    return result3


def inefficient_dictionary_iteration(data_dict):
    """
    BAD: Iterating over dictionary keys and then looking up values
    """
    total = 0
    for key in data_dict.keys():
        total += data_dict[key]
    return total


def inefficient_function_calls_in_loop(data):
    """
    BAD: Calling len() in loop condition (recalculated each iteration)
    """
    result = []
    for i in range(len(data)):
        if i < len(data) - 1:
            result.append(data[i] + data[i + 1])
    return result


def inefficient_global_variable_access():
    """
    BAD: Repeated access to global variables
    Global variable lookup is slower than local variables
    """
    global GLOBAL_MULTIPLIER
    GLOBAL_MULTIPLIER = 2
    result = 0
    for i in range(1000):
        result += i * GLOBAL_MULTIPLIER
    return result


def inefficient_exception_handling(data):
    """
    BAD: Using exceptions for control flow
    Exception handling is expensive
    """
    result = []
    for item in data:
        try:
            value = int(item)
            result.append(value)
        except ValueError:
            pass
    return result


def inefficient_deep_copy(data):
    """
    BAD: Creating unnecessary deep copies
    """
    results = []
    for i in range(100):
        # Making a deep copy when a shallow copy or reference would suffice
        temp = copy.deepcopy(data)
        temp['counter'] = i
        results.append(temp)
    return results


# Global variable for demonstration
GLOBAL_MULTIPLIER = 1


if __name__ == "__main__":
    print("Demonstrating inefficient code patterns...")
    
    # String concatenation
    print("\n1. Testing string concatenation...")
    start = time.time()
    result = inefficient_string_concatenation(range(10000))
    print(f"Time: {time.time() - start:.4f}s")
    
    # List search
    print("\n2. Testing list search...")
    data = list(range(10000))
    start = time.time()
    inefficient_list_search(data, 9999)
    print(f"Time: {time.time() - start:.4f}s")
    
    # Nested loops
    print("\n3. Testing nested loops...")
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    start = time.time()
    result = inefficient_nested_loops(list1, list2)
    print(f"Time: {time.time() - start:.4f}s")
    
    print("\nAll inefficient patterns demonstrated.")
