import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
# print(df)
df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
x = df['date']
y = df['Close']

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].plot(x,y)
axs[1, 0].bar(x,y)
axs[0, 1].scatter(x, y, marker='o', alpha=.5)
axs[1, 1].pie([10, 5], labels=['10', '5'])
plt.show()
