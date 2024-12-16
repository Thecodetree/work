import numpy as np
array_2d = np.array([[1, 2, 3]
                    [4, 5, 6
                    [7, 8, 9]]])

mask_2d = array_2d > 6

result_2d = array_2d[mask_2d]

print("Original Array:")
print(array_2d)

print("\nBoolean Mask:")
print(mask_2d)

print("\nFiltered Elements:")
print("result_2d")