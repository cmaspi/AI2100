import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def normal_hist(img, plot=True):
    arr = np.zeros(256)
    img = img.flatten()
    np.add.at(arr,img,1)
    arr = arr/img.shape[0]
    if plot:
        f = plt.figure()
        ax = f.add_subplot(1,1,1)
        ax.bar(np.arange(256),arr)
    return arr, f if 'f' in locals() else None

img = mpimg.imread('misc/5.1.11.tiff')
count,plot = normal_hist(img)
plot
plt.show()