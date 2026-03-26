import pandas as pd
import numpy as np

n = 30

df = pd.DataFrame({
    "age": np.random.randint(20, 80, n),
    "gender": np.random.choice(["Male", "Female"], n),
    "bp": np.random.randint(110, 180, n),
    "pulse": np.random.randint(60, 110, n),
    "spo2": np.random.randint(90, 100, n),
    "cholesterol": np.random.randint(180, 300, n),
    "diabetes": np.random.choice(["Yes", "No"], n),
    "asthma": np.random.choice(["Yes", "No"], n),
    "thyroid": np.random.choice(["Yes", "No"], n)
})

print(df)

df["risk_level"] = "Low"
df.loc[df["bp"].between(140, 150), "risk_level"] = "Medium"
df.loc[(df["bp"] > 150) | (df["cholesterol"] > 230), "risk_level"] = "High"

df["critical_flag"] = 0
df.loc[df["risk_level"] == "High", "critical_flag"] = 1

print(df)

print(df["risk_level"].value_counts())
print(df[df["risk_level"] == "High"]["bp"].mean())
print(df.groupby("risk_level")["age"].mean())
print(df["diabetes"].value_counts())
print(df.groupby("risk_level")["cholesterol"].mean())