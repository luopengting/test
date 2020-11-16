import numpy as np

nums = np.random.rand(3, 4, 5)

print(nums)
print("========")
print(nums[:, 0, 0])
print(np.var(nums[:, 0, 0]))
print(np.var(nums[:, 0, 1]))
print(np.var(nums, axis=0))
print(np.var(nums, axis=1))
print(np.var(nums, axis=2))
