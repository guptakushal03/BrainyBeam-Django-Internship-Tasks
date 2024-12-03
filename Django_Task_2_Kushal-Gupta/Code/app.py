import time
import numpy as np
from typing import List

complexity_classes = {
    "Constant (O(1))": lambda n: 1,
    "Logarithmic (O(log n))": lambda n: np.log(n),
    "Linear (O(n))": lambda n: n,
    "Linearithmic (O(n log n))": lambda n: n * np.log(n),
    "Quadratic (O(n^2))": lambda n: n ** 2,
    "Cubic (O(n^3))": lambda n: n ** 3,
    "Exponential (O(n!))": lambda n: 2 ** n
}   # Dictionary storing our time complexities

def estimate_complexity(function, input_generator):

    sizes = [10, 20, 40, 80, 160, 320]      # input sizes
    times = []
    
    for size in sizes:
        input_data = input_generator(size)
        
        start_time = time.time()
        function(input_data)
        end_time = time.time()
        
        times.append(max(end_time - start_time, 1e-6))      # makes sure no 0 appended
    
    normalized_times = np.array(times) / max(times[0], 1e-6)
    
    best_match = "Unknown"
    min_diff = float('inf')
    
    for label, growth_func in complexity_classes.items():
        growth_values = np.array([growth_func(n) for n in sizes])
        growth_values = growth_values / max(growth_values[0], 1e-6)
        
        diff = np.linalg.norm(normalized_times - growth_values)
        if diff < min_diff:
            min_diff = diff
            best_match = label
    
    return best_match

def generate_list_input(n):
    return list(range(n))


def example_function(input_data):
    for i in input_data:
        for j in input_data:
            _ = i * j

estimated_complexity = estimate_complexity(example_function, generate_list_input)
print(f"Estimated complexity: {estimated_complexity}")