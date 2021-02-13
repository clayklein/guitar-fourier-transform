import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

em = pd.read_csv(r'csv_data\em_chord.csv')
g = pd.read_csv(r'csv_data\g_chord.csv')
c = pd.read_csv(r'csv_data\c_chord.csv')
d = pd.read_csv(r'csv_data\d_chord.csv')

plt.style.use('dark_background')

fig, ax = plt.subplots(4, sharex=True, sharey=True)

fig.suptitle('Em, G, C, and D Chords', size=25)

for i in range(4):
    ax[i].set_yticks([])

ax[0].set_ylabel('Em Chord', rotation=0, fontsize=15, labelpad=45)
ax[1].set_ylabel('G Chord', rotation=0, fontsize=15, labelpad=45)
ax[2].set_ylabel('C Chord', rotation=0, fontsize=15, labelpad=45)
ax[3].set_ylabel('D Chord', rotation=0, fontsize=15, labelpad=45)

ax[3].set_xlim(0, 4000)
ax[3].set_xticks([500*i for i in range(1,9)])
ax[3].set_xlabel('Frequency (Hz)', fontsize=15)

alpha = .75

ax[0].plot(em['x'], em['y']/np.max(em['y']), label='Em Chord', linewidth=1, c='cyan', alpha=alpha)
ax[1].plot(g['x'], g['y']/np.max(g['y']), label='G Chord', linewidth=1, c='lime', alpha=alpha)
ax[2].plot(c['x'], c['y']/np.max(c['y']), label='C Chord', linewidth=1, c='gold', alpha=alpha)
ax[3].plot(d['x'], d['y']/np.max(d['y']), label='D', linewidth=1, c='orangered', alpha=alpha)

plt.show()
