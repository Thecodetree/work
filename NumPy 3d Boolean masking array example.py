import numpy as np

array_3d = np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]],
                    [[9, 10], [11, 12]]])

mask_3d = (array_3d % 3 == 0)

result_3d = array_3d[mask_3d]

print("Original 3D Array:")
print(array_3d)

print("\nBoolean Mask:")
print(mask_3d)

print("\nFiltered Elements:")
print(result_3d)