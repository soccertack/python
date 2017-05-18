import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

gs = mpl.gridspec.GridSpec(2, 1)
gs.update(wspace=0.1, hspace=0.01)

plt.subplot(gs[0])
frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
plt.plot(np.arange(10),np.random.random([10]),color='deeppink')


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
