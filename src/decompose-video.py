import matplotlib.pylab as pl
import matplotlib.patches as mpatches
import numpy as np
import imageio
import skimage.color
import skimage.measure

filename = "../videos/input.m4v"
video = imageio.get_reader(filename, "ffmpeg")
frame_ranges_L = [(1200, 1850), (2200, 2880)]
frame_ranges_R = [(3170, 3800), (4200, 4920)]
BRIGHTNESS_THRESHOLD = .95
light_centers = []

print("Finding light centers")
pl.set_cmap("gray")
current_frame = None
for i, im in enumerate(video):
    if i<1200: continue

    pl.title("frame {}".format(i), fontsize=20)

    # TODO-P2: Gaussian blur before thresholding

    # Convert image to grayscale
    grayscale = skimage.color.rgb2gray(im)
    # Create thresholded image from grayscale
    thresholded = np.zeros(grayscale.shape)
    thresholded[:,:] = (grayscale > BRIGHTNESS_THRESHOLD)

    # TODO-P1: Erosion/dilation to get rid of small dots
    #thresholded_opening = skimage.morphology.binary_opening(thresholded)

    # TODO-P1: Pull this out of the render loop
    labeled = skimage.measure.label(thresholded)
    labeled_rgb = skimage.color.label2rgb(labeled)
    # TODO-P0: Track light source by finding the connected component most similar to last known light source component

    if current_frame is None:
        current_frame = pl.imshow(labeled_rgb)
        #current_frame = pl.imshow(im)
    else:
        current_frame.set_data(labeled_rgb)
        #current_frame.set_data(im)

    pl.pause(.01)
    pl.draw()

