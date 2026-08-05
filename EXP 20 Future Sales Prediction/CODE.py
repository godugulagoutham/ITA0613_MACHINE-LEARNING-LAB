# EXPERIMENT NO 20 Future Sales Prediction using a suitable machine learning algorithm

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

data = pd.DataFrame({
    'Age':[20,25,30,35,40],
    'Salary':[20000,30000,40000,50000,60000]
})

print("Before Scaling:\n",data)

scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)
scaled_df = pd.DataFrame(scaled,columns=data.columns)

print("After Scaling:\n",scaled_df)

data.hist()
plt.title("Before Scaling")
plt.show()

scaled_df.hist()
plt.title("After Scaling")
plt.show()
