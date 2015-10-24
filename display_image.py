import numpy as np
from matplotlib import pyplot as plt
import sys

file  = sys.argv[2]
line_num = int(sys.argv[4])

fp = open(file)
for i, line in enumerate(fp):
    if i == line_num:
        data = line.split(",")[1]
fp.close()

data  = np.fromstring(data, dtype=int, sep=' ')
data = np.reshape(data, (48, 48))
plt.imshow(data, cmap = 'gray')
plt.show()