import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("merged_data.csv")
#print(data.head())
#date = data["DateTime"]
#lat1 = data["21.5_85.5"]
#plt.figure(figsize=(10, 5))
#plt.plot(date,lat1)
#plt.show()
hot_days = data[data.iloc[:, 1] > 40.0]
hot_dates = hot_days["DateTime"]
print("Dates when Tmax > 40.0:")
print(hot_dates.tolist())