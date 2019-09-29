import skimage.io as io
from skimage.color import rgb2gray
gambar = input("Drag gambar kesini!")
src = len(gambar)
name = gambar[0:(src-4)]
format = gambar[-4:]
img = io.imread(gambar)
img_grayscale = rgb2gray(img)
io.imsave(name+'-gs'+format, img_grayscale)

show_grayscale = io.imshow(img_grayscale)
io.show()
