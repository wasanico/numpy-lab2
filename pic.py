from PIL import Image
import numpy as np

# Open the image form working directory
image = Image.open('face.png')
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)


# convert image to numpy array
data = np.asarray(image)
print(type(data)) 
print(data.shape)  

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))
image2
# summarize image 2 details
print(image2.size)
print(image2.mode)
print(data)

#image.show()