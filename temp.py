import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV file
df = pd.read_csv("data.csv")

# Pivot the DataFrame for better plotting
df_pivot = df.pivot(index="A", columns="B", values="speedup")

# Plotting
df_pivot.plot(kind="bar", width=0.8)
plt.title("Speedup by Prefetcher and Benchmark")
plt.xlabel("Benchmark (A)")
plt.ylabel("Speedup")

# Set the y-axis limit to start from a higher value for clarity
plt.ylim(0.99, 1.01)  # Adjust the range as needed

plt.legend(title="Prefetcher (B)", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# Display the plot
plt.show()
