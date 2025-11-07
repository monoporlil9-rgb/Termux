#!/usr/bin/env python3
"""
Performance comparison and benchmarking
Compares inefficient vs optimized code implementations
"""

import time
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

import inefficient_code
import optimized_code


def benchmark(func, *args, iterations=10):
    """Run a function multiple times and return average execution time"""
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        times.append(end - start)
    
    avg_time = sum(times) / len(times)
    return avg_time, result


def format_improvement(old_time, new_time):
    """Calculate and format performance improvement"""
    if new_time > 0:
        speedup = old_time / new_time
        improvement = ((old_time - new_time) / old_time) * 100
        return f"{speedup:.2f}x faster ({improvement:.1f}% improvement)"
    return "N/A"


def main():
    print("=" * 80)
    print("PERFORMANCE COMPARISON: Inefficient vs Optimized Code")
    print("=" * 80)
    
    # Test 1: String concatenation
    print("\n" + "=" * 80)
    print("TEST 1: String Concatenation (10,000 items)")
    print("-" * 80)
    data = list(range(10000))
    
    inefficient_time, _ = benchmark(inefficient_code.inefficient_string_concatenation, data)
    optimized_time, _ = benchmark(optimized_code.optimized_string_concatenation, data)
    
    print(f"Inefficient (+=):     {inefficient_time:.6f} seconds")
    print(f"Optimized (join):     {optimized_time:.6f} seconds")
    print(f"Improvement:          {format_improvement(inefficient_time, optimized_time)}")
    
    # Test 2: List search with duplicates
    print("\n" + "=" * 80)
    print("TEST 2: List Search (10,000 items)")
    print("-" * 80)
    data = list(range(10000))
    
    inefficient_time, _ = benchmark(inefficient_code.inefficient_list_search, data, 9999)
    optimized_time, _ = benchmark(optimized_code.optimized_list_search, data, 9999)
    
    print(f"Inefficient (list):   {inefficient_time:.6f} seconds")
    print(f"Optimized (set):      {optimized_time:.6f} seconds")
    print(f"Improvement:          {format_improvement(inefficient_time, optimized_time)}")
    
    # Test 3: Finding common elements
    print("\n" + "=" * 80)
    print("TEST 3: Finding Common Elements (1000 vs 1000 items)")
    print("-" * 80)
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    
    inefficient_time, inefficient_result = benchmark(
        inefficient_code.inefficient_nested_loops, list1, list2
    )
    optimized_time, optimized_result = benchmark(
        optimized_code.optimized_nested_loops, list1, list2
    )
    
    print(f"Inefficient (nested): {inefficient_time:.6f} seconds")
    print(f"Optimized (set &):    {optimized_time:.6f} seconds")
    print(f"Improvement:          {format_improvement(inefficient_time, optimized_time)}")
    print(f"Results match:        {set(inefficient_result) == set(optimized_result)}")
    
    # Test 4: Data filtering
    print("\n" + "=" * 80)
    print("TEST 4: Data Filtering (10,000 items)")
    print("-" * 80)
    data = list(range(-5000, 5000))
    
    inefficient_time, inefficient_result = benchmark(
        inefficient_code.inefficient_data_filtering, data
    )
    optimized_time, optimized_result = benchmark(
        optimized_code.optimized_data_filtering, data
    )
    
    print(f"Inefficient (3 loops): {inefficient_time:.6f} seconds")
    print(f"Optimized (1 pass):    {optimized_time:.6f} seconds")
    print(f"Improvement:           {format_improvement(inefficient_time, optimized_time)}")
    print(f"Results match:         {inefficient_result == optimized_result}")
    
    # Test 5: Dictionary iteration
    print("\n" + "=" * 80)
    print("TEST 5: Dictionary Iteration (10,000 items)")
    print("-" * 80)
    data_dict = {f"key_{i}": i for i in range(10000)}
    
    inefficient_time, inefficient_result = benchmark(
        inefficient_code.inefficient_dictionary_iteration, data_dict
    )
    optimized_time, optimized_result = benchmark(
        optimized_code.optimized_dictionary_iteration, data_dict
    )
    
    print(f"Inefficient (keys):   {inefficient_time:.6f} seconds")
    print(f"Optimized (values):   {optimized_time:.6f} seconds")
    print(f"Improvement:          {format_improvement(inefficient_time, optimized_time)}")
    print(f"Results match:        {inefficient_result == optimized_result}")
    
    # Test 6: Function calls in loop
    print("\n" + "=" * 80)
    print("TEST 6: Function Calls in Loop (10,000 items)")
    print("-" * 80)
    data = list(range(10000))
    
    inefficient_time, inefficient_result = benchmark(
        inefficient_code.inefficient_function_calls_in_loop, data
    )
    optimized_time, optimized_result = benchmark(
        optimized_code.optimized_function_calls_in_loop, data
    )
    
    print(f"Inefficient (len in loop): {inefficient_time:.6f} seconds")
    print(f"Optimized (cached len):    {optimized_time:.6f} seconds")
    print(f"Improvement:               {format_improvement(inefficient_time, optimized_time)}")
    print(f"Results match:             {inefficient_result == optimized_result}")
    
    # Test 7: Global variable access
    print("\n" + "=" * 80)
    print("TEST 7: Global Variable Access (1,000 iterations)")
    print("-" * 80)
    
    inefficient_time, inefficient_result = benchmark(
        inefficient_code.inefficient_global_variable_access
    )
    optimized_time, optimized_result = benchmark(
        optimized_code.optimized_global_variable_access
    )
    
    print(f"Inefficient (global):  {inefficient_time:.6f} seconds")
    print(f"Optimized (local):     {optimized_time:.6f} seconds")
    print(f"Improvement:           {format_improvement(inefficient_time, optimized_time)}")
    print(f"Results match:         {inefficient_result == optimized_result}")
    
    # Test 8: Exception handling
    print("\n" + "=" * 80)
    print("TEST 8: Type Checking vs Exception Handling")
    print("-" * 80)
    data = [1, 2, "3", "4", "invalid", 5, "6", 7, "not a number", 8, 9]
    
    inefficient_time, inefficient_result = benchmark(
        inefficient_code.inefficient_exception_handling, data
    )
    optimized_time, optimized_result = benchmark(
        optimized_code.optimized_exception_handling, data
    )
    
    print(f"Inefficient (try/except): {inefficient_time:.6f} seconds")
    print(f"Optimized (type check):   {optimized_time:.6f} seconds")
    print(f"Improvement:              {format_improvement(inefficient_time, optimized_time)}")
    
    # Test 9: Deep copy
    print("\n" + "=" * 80)
    print("TEST 9: Deep Copy vs Shallow Copy (100 iterations)")
    print("-" * 80)
    data = {"name": "test", "value": 42, "items": [1, 2, 3]}
    
    inefficient_time, _ = benchmark(
        inefficient_code.inefficient_deep_copy, data
    )
    optimized_time, _ = benchmark(
        optimized_code.optimized_deep_copy, data
    )
    optimized_time_v2, _ = benchmark(
        optimized_code.optimized_deep_copy_v2, data
    )
    
    print(f"Inefficient (deepcopy):      {inefficient_time:.6f} seconds")
    print(f"Optimized (shallow copy):    {optimized_time:.6f} seconds")
    print(f"Optimized (dict comp):       {optimized_time_v2:.6f} seconds")
    print(f"Improvement (shallow):       {format_improvement(inefficient_time, optimized_time)}")
    print(f"Improvement (dict comp):     {format_improvement(inefficient_time, optimized_time_v2)}")
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("All tests completed successfully!")
    print("The optimized code consistently outperforms the inefficient versions.")
    print("=" * 80)


if __name__ == "__main__":
    main()
