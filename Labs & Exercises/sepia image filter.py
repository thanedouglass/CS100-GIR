import common
import numpy as np
def sepia(image_array):

  # Convert the input image list to a NumPy array
    sepia_image = np.array(image_array)

    # Define the sepia filter coefficients
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])

    # Get the dimensions of the image
    num_rows, num_cols, num_channels = sepia_image.shape

    # Apply the sepia filter to each pixel
    for i in range(num_rows):
        for j in range(num_cols):
            pixel = sepia_image[i, j]
            new_pixel = np.zeros_like(pixel)
            for channel in range(num_channels):
                new_value = 0
                for k in range(num_channels):
                    new_value += pixel[k] * sepia_filter[channel, k]
                new_pixel[channel] = min(255, int(new_value))
            sepia_image[i, j] = new_pixel
    
    return sepia_image

image = common.read_file("redtrio.jpg")

# Apply the sepia filter to the image
sepia_image = sepia(image)

# Save the sepia-processed image
common.write_file("sepia_redtrio.jpg", sepia_image)

