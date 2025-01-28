import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\shahi\Downloads\weight-height.csv"

data = pd.read_csv(file_path)

lengths_in_inches = data['Height'].values
weights_in_pounds = data['Weight'].values

lengths_in_cm = lengths_in_inches * 2.54
weights_in_kg = weights_in_pounds * 0.453592

mean_length_cm = np.mean(lengths_in_cm)
mean_weight_kg = np.mean(weights_in_kg)

print(f"Mean Length: {mean_length_cm:.2f} cm")
print(f"Mean Weight: {mean_weight_kg:.2f} kg")

plt.hist(lengths_in_cm, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Lengths (cm)')
plt.xlabel('Length (cm)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()
