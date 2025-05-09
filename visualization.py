import pandas as pd
import matplotlib.pyplot as plt 
import os


data = pd.read_csv('simulated_physiological_data.csv')
# print(data.head())

fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)


axs[0].plot(data['HeartRate'], color='red')
axs[0].set_title('Heart Rate')
axs[0].set_ylabel('Breaths per minute')
axs[0].set_ylim(50, 160)
axs[0].grid(True)

axs[1].plot(data['Temperature'], color='orange')
axs[1].set_title('Body Temperature')
axs[1].set_ylabel('Celcius')
axs[1].set_ylim(35, 40)
axs[1].grid(True)

axs[2].plot(data['SpO2'], color='blue')
axs[2].set_title('Oxygen Level')
axs[2].set_ylabel('Percentage')
axs[2].set_ylim(85, 105)
axs[2].set_xlabel('Sample')
axs[2].grid(True)

plt.tight_layout()
plt.show()


# abnormals_heart_rates = data['HeartRate'] > 120

# print(abnormals_heart_rates)
