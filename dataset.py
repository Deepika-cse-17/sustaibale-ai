import pandas as pd
import numpy as np

# For reproducibility
np.random.seed(42)

# Simulated mobile sensor data
data = {
    "steps_per_day": np.random.randint(1000, 12000, 200),
    "screen_time_hours": np.random.uniform(1, 10, 200),
    "sleep_hours": np.random.uniform(4, 9, 200),
    "movement_variance": np.random.uniform(0.1, 2.5, 200),
    "heart_rate_variation": np.random.uniform(50, 100, 200)
}

df = pd.DataFrame(data)

# Assign wellbeing level automatically
def assign_wellbeing(row):
    if row["sleep_hours"] >= 7 and row["steps_per_day"] >= 7000:
        return 2   # Good
    elif row["sleep_hours"] >= 5:
        return 1   # Moderate
    else:
        return 0   # Low

df["wellbeing_level"] = df.apply(assign_wellbeing, axis=1)

# Save dataset
df.to_csv("women_wellbeing_data.csv", index=False)

print("Dataset created successfully!")
