# Day 45 - NumPy vs Python Lists Speed Test
# Prove why NumPy is essential

import numpy as np
import time

print("="*60)
print("SPEED TEST: NUMPY VS PYTHON LISTS")
print("="*60)

# Create large dataset
size = 1_000_000
print(f"\nDataset size: {size:,} elements")

# Python list approach
print("\n--- PYTHON LISTS ---")
py_list = list(range(size))

start = time.time()
# Calculate 10% discount
discounted_list = [price * 0.9 for price in py_list]
end = time.time()
py_time = end - start
print(f"Time taken: {py_time:.4f} seconds")

# NumPy approach
print("\n--- NUMPY ARRAY ---")
np_array = np.arange(size)

start = time.time()
# Calculate 10% discount
discounted_array = np_array * 0.9
end = time.time()
np_time = end - start
print(f"Time taken: {np_time:.4f} seconds")

# Comparison
print("\n" + "="*60)
print("RESULTS")
print("="*60)
speedup = py_time / np_time
print(f"NumPy is {speedup:.1f}x FASTER!")
print(f"Time saved: {(py_time - np_time):.4f} seconds")

# Real-world context
print(f"\n💡 Real-world impact:")
print(f"If you process this 100 times a day:")
print(f"  Python lists: {py_time * 100:.2f} seconds ({py_time * 100 / 60:.2f} minutes)")
print(f"  NumPy: {np_time * 100:.2f} seconds ({np_time * 100 / 60:.2f} minutes)")
print(f"  Time saved per day: {(py_time - np_time) * 100 / 60:.2f} minutes")

print("\n" + "="*60)
print("THIS IS WHY DATA ANALYSTS USE NUMPY! ✅")
print("="*60)