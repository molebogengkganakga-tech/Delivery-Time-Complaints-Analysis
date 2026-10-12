import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 1. Create the dataset
data = {
    "Day": list(range(1, 13)),
    "Delivery_Time": [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
    "Complaints": [2, 3, 5, 4, 6, 8, 10, 9, 11, 13, 12, 14]
}

df = pd.DataFrame(data)
df.to_csv("delivery_data.csv", index=False)

# 2. Explore the data
print("DELIVERY TIME & CUSTOMER COMPLAINTS ANALYSIS")
print("=" * 45)
print("\nFirst five rows:")
print(df.head())

print("\nSummary statistics:")
print(df[["Delivery_Time", "Complaints"]].describe().round(2))

# 3. Calculate Pearson correlation
correlation, p_value = stats.pearsonr(
    df["Delivery_Time"],
    df["Complaints"]
)

print("\nCORRELATION RESULTS")
print(f"Pearson correlation: {correlation:.3f}")
print(f"P-value: {p_value:.4f}")

# 4. Fit a linear regression model
slope, intercept, r_value, p_value, std_err = stats.linregress(
    df["Delivery_Time"],
    df["Complaints"]
)

print("\nLINEAR REGRESSION RESULTS")
print(f"Slope: {slope:.3f}")
print(f"Intercept: {intercept:.3f}")
print(f"R-squared: {r_value**2:.3f}")

# 5. Predict complaints at 82 minutes
delivery_time = 82
predicted_complaints = intercept + slope * delivery_time

print(f"\nPredicted complaints at {delivery_time} minutes: "
      f"{predicted_complaints:.2f}")

# 6. Create a scatter plot and regression line
plt.figure(figsize=(9, 6))

plt.scatter(
    df["Delivery_Time"],
    df["Complaints"],
    color="royalblue",
    label="Observed data"
)

plt.plot(
    df["Delivery_Time"],
    intercept + slope * df["Delivery_Time"],
    color="darkorange",
    label="Linear regression"
)

plt.title("Delivery Time vs Customer Complaints")
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Number of Complaints")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Save the chart in the project folder
plt.savefig("correlation_analysis.png", dpi=300)
plt.show()