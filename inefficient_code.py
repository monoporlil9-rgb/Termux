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
    concatenated_string = ""
    for current_item in items:
        concatenated_string += str(current_item) + ","
    return concatenated_string


def inefficient_list_search(data, target):
    """
    BAD: Using list for frequent membership checks
    List lookup is O(n) for each check
    """
    seen_items = []
    for current_item in data:
        if current_item not in seen_items:
            seen_items.append(current_item)
        if current_item == target:
            return True
    return False


def inefficient_nested_loops(first_list, second_list):
    """
    BAD: Nested loops for finding common elements
    O(n*m) time complexity
    """
    common_elements = []
    for first_item in first_list:
        for second_item in second_list:
            if first_item == second_item and first_item not in common_elements:
                common_elements.append(first_item)
    return common_elements


def inefficient_file_reading(filename):
    """
    BAD: Reading file line by line with repeated disk I/O
    """
    file_lines = []
    with open(filename, 'r') as file_handle:
        current_line = file_handle.readline()
        while current_line:
            file_lines.append(current_line.strip())
            current_line = file_handle.readline()
    return file_lines


def inefficient_data_filtering(data):
    """
    BAD: Multiple passes over the data
    Each filter creates a new list
    """
    positive_numbers = []
    for number in data:
        if number > 0:
            positive_numbers.append(number)
    
    even_positive_numbers = []
    for number in positive_numbers:
        if number % 2 == 0:
            even_positive_numbers.append(number)
    
    doubled_even_numbers = []
    for number in even_positive_numbers:
        doubled_even_numbers.append(number * 2)
    
    return doubled_even_numbers


def inefficient_dictionary_iteration(data_dict):
    """
    BAD: Iterating over dictionary keys and then looking up values
    """
    running_total = 0
    for dict_key in data_dict.keys():
        running_total += data_dict[dict_key]
    return running_total


def inefficient_function_calls_in_loop(data):
    """
    BAD: Calling len() in loop condition (recalculated each iteration)
    """
    pairwise_sums = []
    for index in range(len(data)):
        if index < len(data) - 1:
            pairwise_sums.append(data[index] + data[index + 1])
    return pairwise_sums


def inefficient_global_variable_access():
    """
    BAD: Repeated access to global variables
    Global variable lookup is slower than local variables
    """
    global GLOBAL_MULTIPLIER
    GLOBAL_MULTIPLIER = 2
    accumulated_sum = 0
    for counter in range(1000):
        accumulated_sum += counter * GLOBAL_MULTIPLIER
    return accumulated_sum


def inefficient_exception_handling(data):
    """
    BAD: Using exceptions for control flow
    Exception handling is expensive
    """
    converted_integers = []
    for data_element in data:
        try:
            integer_value = int(data_element)
            converted_integers.append(integer_value)
        except ValueError:
            pass
    return converted_integers


def inefficient_deep_copy(data):
    """
    BAD: Creating unnecessary deep copies
    """
    modified_dicts = []
    for iteration_count in range(100):
        # Making a deep copy when a shallow copy or reference would suffice
        copied_dict = copy.deepcopy(data)
        copied_dict['counter'] = iteration_count
        modified_dicts.append(copied_dict)
    return modified_dicts


# Global variable for demonstration
GLOBAL_MULTIPLIER = 1


if __name__ == "__main__":
    print("Demonstrating inefficient code patterns...")
    
    # String concatenation
    print("\n1. Testing string concatenation...")
    start_time = time.time()
    concatenation_result = inefficient_string_concatenation(range(10000))
    print(f"Time: {time.time() - start_time:.4f}s")
    
    # List search
    print("\n2. Testing list search...")
    search_data = list(range(10000))
    start_time = time.time()
    inefficient_list_search(search_data, 9999)
    print(f"Time: {time.time() - start_time:.4f}s")
    
    # Nested loops
    print("\n3. Testing nested loops...")
    first_number_list = list(range(1000))
    second_number_list = list(range(500, 1500))
    start_time = time.time()
    common_result = inefficient_nested_loops(first_number_list, second_number_list)
    print(f"Time: {time.time() - start_time:.4f}s")
    
    print("\nAll inefficient patterns demonstrated.")
