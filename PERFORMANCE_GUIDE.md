# Performance Optimization Guide

This repository contains examples of slow/inefficient code patterns and their optimized alternatives, demonstrating common performance issues and how to fix them.

## Overview

Performance optimization is crucial for creating efficient applications. This guide identifies common anti-patterns that lead to slow code and provides best practices for writing performant code.

## Files

- `inefficient_code.py` - Examples of common performance anti-patterns
- `optimized_code.py` - Optimized versions of the same functionality
- `performance_comparison.py` - Benchmarking tool to compare performance
- `PERFORMANCE_GUIDE.md` - Detailed guide on optimization techniques

## Quick Start

Run the performance comparison to see the difference:

```bash
python3 performance_comparison.py
```

## Common Performance Issues Identified

### 1. String Concatenation in Loops ❌

**Problem:** Using `+=` for string concatenation creates a new string object each iteration.

```python
# BAD - O(n²) complexity
result = ""
for item in items:
    result += str(item) + ","
```

**Solution:** Use `join()` which is O(n) complexity.

```python
# GOOD - O(n) complexity
result = ",".join(str(item) for item in items)
```

**Performance Gain:** ~100-200x faster for large datasets

---

### 2. List Membership Checks ❌

**Problem:** Using `in` operator on lists has O(n) time complexity.

```python
# BAD - O(n) lookup per operation
seen = []
if item not in seen:
    seen.append(item)
```

**Solution:** Use sets which have O(1) average lookup time.

```python
# GOOD - O(1) lookup per operation
seen = set()
if item not in seen:
    seen.add(item)
```

**Performance Gain:** ~50-100x faster for large datasets

---

### 3. Nested Loops for Finding Common Elements ❌

**Problem:** Nested loops create O(n×m) time complexity.

```python
# BAD - O(n*m) complexity
common = []
for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            common.append(item1)
```

**Solution:** Use set intersection which is O(n + m) complexity.

```python
# GOOD - O(n+m) complexity
common = list(set(list1) & set(list2))
```

**Performance Gain:** ~50-100x faster for large lists

---

### 4. Multiple Passes Over Data ❌

**Problem:** Processing data in multiple separate loops.

```python
# BAD - Multiple passes
result = []
for item in data:
    if item > 0:
        result.append(item)

result2 = []
for item in result:
    if item % 2 == 0:
        result2.append(item)
```

**Solution:** Process in a single pass using list comprehension.

```python
# GOOD - Single pass
result = [item for item in data if item > 0 and item % 2 == 0]
```

**Performance Gain:** ~2-3x faster

---

### 5. Redundant Dictionary Lookups ❌

**Problem:** Iterating over keys and then looking up values.

```python
# BAD - Double lookup
total = 0
for key in data_dict.keys():
    total += data_dict[key]
```

**Solution:** Use `.values()` or `.items()` directly.

```python
# GOOD - Direct access
total = sum(data_dict.values())
```

**Performance Gain:** ~30-40% faster

---

### 6. Function Calls in Loop Conditions ❌

**Problem:** Calling functions like `len()` on every loop iteration.

```python
# BAD - len() called repeatedly
for i in range(len(data)):
    if i < len(data) - 1:
        # ...
```

**Solution:** Cache the result in a variable.

```python
# GOOD - Cache the length
data_len = len(data)
for i in range(data_len - 1):
    # ...
```

**Performance Gain:** ~10-20% faster

---

### 7. Global Variable Access in Loops ❌

**Problem:** Accessing global variables is slower than local variables.

```python
# BAD - Global access in loop
for i in range(1000):
    result += i * GLOBAL_MULTIPLIER
```

**Solution:** Cache global variables as local.

```python
# GOOD - Cache as local
multiplier = GLOBAL_MULTIPLIER
for i in range(1000):
    result += i * multiplier
```

**Performance Gain:** ~15-25% faster

---

### 8. Exceptions for Control Flow ❌

**Problem:** Exception handling is expensive.

```python
# BAD - Using exceptions for control flow
for item in data:
    try:
        value = int(item)
        result.append(value)
    except ValueError:
        pass
```

**Solution:** Check types before conversion.

```python
# GOOD - Type checking
for item in data:
    if isinstance(item, int):
        result.append(item)
    elif isinstance(item, str) and item.isdigit():
        result.append(int(item))
```

**Performance Gain:** ~5-10x faster

---

### 9. Unnecessary Deep Copies ❌

**Problem:** Deep copying when shallow copy would suffice.

```python
# BAD - Unnecessary deep copy
import copy
for i in range(100):
    temp = copy.deepcopy(data)
    temp['counter'] = i
```

**Solution:** Use shallow copy or dictionary unpacking.

```python
# GOOD - Shallow copy
for i in range(100):
    temp = {**data, 'counter': i}
```

**Performance Gain:** ~10-50x faster

---

### 10. Inefficient File I/O ❌

**Problem:** Reading files line by line with repeated disk I/O.

```python
# BAD - Multiple read operations
lines = []
line = f.readline()
while line:
    lines.append(line.strip())
    line = f.readline()
```

**Solution:** Read all at once or use list comprehension.

```python
# GOOD - Single read operation
lines = [line.strip() for line in f]
```

**Performance Gain:** ~20-30% faster

---

## General Performance Best Practices

### 1. Choose the Right Data Structure
- Use `set` for membership testing
- Use `dict` for key-value lookups
- Use `list` for ordered sequences
- Use `deque` for queue operations

### 2. Avoid Premature Optimization
- Profile your code first
- Focus on bottlenecks
- Measure improvements

### 3. Use Built-in Functions
- Built-in functions are implemented in C
- They're faster than pure Python equivalents
- Examples: `sum()`, `max()`, `min()`, `any()`, `all()`

### 4. List Comprehensions vs Loops
- List comprehensions are generally faster
- More Pythonic and readable
- Use generator expressions for memory efficiency

### 5. Cache Expensive Operations
- Store results of expensive calculations
- Use `functools.lru_cache` for memoization
- Cache database queries

### 6. Minimize Function Call Overhead
- Move invariant code outside loops
- Use local variables instead of globals
- Inline simple operations when performance critical

## Profiling Tools

### Time Measurement
```python
import time
start = time.perf_counter()
# ... code to measure ...
elapsed = time.perf_counter() - start
```

### Memory Profiling
```python
import tracemalloc
tracemalloc.start()
# ... code to measure ...
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
```

### cProfile
```bash
python -m cProfile -s cumulative your_script.py
```

### line_profiler
```bash
kernprof -l -v your_script.py
```

## Running the Benchmarks

To see the performance improvements:

```bash
# Run all benchmarks
python3 performance_comparison.py

# Run individual tests
python3 inefficient_code.py
python3 optimized_code.py
```

## Expected Results

On a typical modern system, you should see:

| Test | Inefficient | Optimized | Speedup |
|------|-------------|-----------|---------|
| String Concatenation | ~2.5s | ~0.001s | ~2500x |
| List Search | ~1.5s | ~0.002s | ~750x |
| Nested Loops | ~0.5s | ~0.001s | ~500x |
| Data Filtering | ~0.003s | ~0.001s | ~3x |
| Dict Iteration | ~0.002s | ~0.001s | ~2x |
| Function Calls | ~0.002s | ~0.0015s | ~1.3x |
| Global Access | ~0.0002s | ~0.00015s | ~1.3x |
| Exception Handling | ~0.0003s | ~0.00003s | ~10x |
| Deep Copy | ~0.02s | ~0.0005s | ~40x |

## Contributing

Feel free to add more examples of performance anti-patterns and their optimizations.

## License

This is a demonstration repository for educational purposes.
