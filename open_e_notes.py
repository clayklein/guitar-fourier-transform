import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

low_e = pd.read_csv(r'csv_data\low_e.csv')
a = pd.read_csv(r'csv_data\a.csv')
d = pd.read_csv(r'csv_data\d.csv')
g = pd.read_csv(r'csv_data\g.csv')
b = pd.read_csv(r'csv_data\b.csv')
high_e = pd.read_csv(r'csv_data\high_e.csv')

#plt.style.use('dark_background')

fig1, ax = plt.subplots()

ax.set_xlim(0, 2000)
ax.set_title('Open Notes')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude')
ax.axes.yaxis.set_ticks([])

alpha=.6

ax.plot(low_e['x'], low_e['y']/np.max(low_e['y']), label='Low E', linewidth=1, c='magenta', alpha=alpha)
ax.plot(high_e['x'], high_e['y']/np.max(high_e['y']), label='High E', linewidth=1, c='red', alpha=alpha)

ax.legend()

plt.show()

fig2, ax = plt.subplots(2, sharex=True)

fig2.suptitle('Open Notes', size=25)

for i in range(2):
    ax[i].set_yticks([])

ax[0].set_ylabel('Low E', rotation=0, fontsize=15, labelpad=50)
ax[1].set_ylabel('High E', rotation=0, fontsize=15, labelpad=50)


ax[1].set_xlim(0, 10000)
ax[1].set_xticks([500*i for i in range(1,21)])
ax[1].set_xlabel('Frequency (Hz)', fontsize=15)

ax[0].plot(low_e['x'], low_e['y']/np.max(low_e['y']), label='low E', linewidth=1, c='magenta', alpha=alpha)
ax[1].plot(high_e['x'], high_e['y']/np.max(high_e['y']), label='High E', linewidth=1, c='red', alpha=alpha)

plt.show()