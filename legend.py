import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import sys

macro_data = pd.read_csv('macro.csv')
#print (macro_data)
print (macro_data['x86 Nested'])
print (macro_data.shape)

gs = mpl.gridspec.GridSpec(2, 1)
gs.update(wspace=0.1, hspace=0.01)

plt.subplot(gs[0])
frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
plt.plot(np.arange(10),np.random.random([10]),color='deeppink')

#n_groups: num of applications
n_groups = macro_data.shape[0]

config_names = list(macro_data)[1:]
print (config_names)
for i, config in enumerate(config_names):
	means_frank = macro_data[config]
	index = np.arange(n_groups)
	bar_width = 0.1
	rects1 = plt.bar(index+i*bar_width, means_frank, bar_width,
			 color='b',
			 label='Frank')


plt.subplot(gs[1])
frame2 = plt.gca()
frame2.axes.spines['top'].set_visible(False)
plt.plot(np.arange(10),np.random.random([10]),color='g')

red_patch0 = mpatches.Patch(color='red', label='The red data0')
red_patch1 = mpatches.Patch(color='red', label='The red data1')
red_patch2 = mpatches.Patch(color='red', label='The red data2')
red_patch3 = mpatches.Patch(color='red', label='The red data3')
blue_patch0 = mpatches.Patch(color='blue', label='The blue data0')
blue_patch1 = mpatches.Patch(color='blue', label='The blue data1')
blue_patch2 = mpatches.Patch(color='w', label='')
plt.legend(handles=[red_patch0, red_patch1, red_patch2, red_patch3, blue_patch0, blue_patch1, blue_patch2], ncol=2)

plt.show()
