import skimage.io as io
from skimage.color import rgb2gray
img = io.imread('sheep.jpg')
img_grayscale = rgb2gray(img)
io.imsave('sheep-gs.jpg', img_grayscale)

show_grayscale = io.imshow(img_grayscale)
io.show()