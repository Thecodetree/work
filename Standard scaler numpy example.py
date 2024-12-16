from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.0, 9.0]])

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)

print("Original Data:\n", data)
print("\nScaled Data:\n", scaled_data)

print("\nMean of features\n", scaler.mean_)
print("Scale of features:\n", scaler.scale_)