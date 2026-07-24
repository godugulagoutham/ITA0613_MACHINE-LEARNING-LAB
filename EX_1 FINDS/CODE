#EXPERIMENT (1)_FIND S
import pandas as pd
data = {
    "Sky": ["Sunny", "Sunny", "Rainy", "Sunny"],
    "AirTemp": ["Warm", "Warm", "Cold", "Warm"],
    "Humidity": ["Normal", "High", "High", "High"],
    "Wind": ["Strong", "Strong", "Strong", "Strong"],
    "Forecast": ["Same", "Same", "Change", "Same"],
    "EnjoySport": ["Yes", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)
hypothesis = ['0'] * (len(df.columns) - 1)
print("Initial Hypothesis:", hypothesis)

for i, row in df.iterrows():
    if row["EnjoySport"] == "Yes":
        for j in range(len(hypothesis)):
            if hypothesis[j] == '0':
                hypothesis[j] = row.iloc[j]
            elif hypothesis[j] != row.iloc[j]:
                hypothesis[j] = '?'
    print(f"After instance {i+1}: {hypothesis}")

print("Final Hypothesis:", hypothesis)
