import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

low_e = pd.read_csv(r'csv_data\low_e.csv')
a = pd.read_csv(r'csv_data\a.csv')
d = pd.read_csv(r'csv_data\d.csv')
g = pd.read_csv(r'csv_data\g.csv')
b = pd.read_csv(r'csv_data\b.csv')
high_e = pd.read_csv(r'csv_data\high_e.csv')

plt.style.use('dark_background')

fig, ax = plt.subplots(6, sharex=True, sharey=True)

fig.suptitle('Open Notes', size=25)

alpha = .6

for i in range(6):
    ax[i].set_yticks([])

ax[0].set_ylabel('Low E', rotation=0, fontsize=15, labelpad=50)
ax[1].set_ylabel('A', rotation=0, fontsize=15, labelpad=45)
ax[2].set_ylabel('D', rotation=0, fontsize=15, labelpad=45)
ax[3].set_ylabel('G', rotation=0, fontsize=15, labelpad=45)
ax[4].set_ylabel('B', rotation=0, fontsize=15, labelpad=45)
ax[5].set_ylabel('High E', rotation=0, fontsize=15, labelpad=50)

ax[5].set_xlim(0, 10000)
ax[5].set_xticks([500*i for i in range(1,21)])
ax[5].set_xlabel('Frequency (Hz)', fontsize=15)

ax[0].plot(low_e['x'], low_e['y']/np.max(low_e['y']), label='Low E', linewidth=1, c='magenta', alpha=alpha)
ax[1].plot(a['x'], a['y']/np.max(a['y']), label='A', linewidth=1, c='cyan', alpha=alpha)
ax[2].plot(d['x'], d['y']/np.max(d['y']), label='D', linewidth=1, c='lime', alpha=alpha)
ax[3].plot(g['x'], g['y']/np.max(g['y']), label='G', linewidth=1, c='gold', alpha=alpha)
ax[4].plot(b['x'], b['y']/np.max(b['y']), label='B', linewidth=1, c='orangered', alpha=alpha)
ax[5].plot(high_e['x'], high_e['y']/np.max(high_e['y']), label='High E', linewidth=1, c='red', alpha=alpha)

plt.show()
