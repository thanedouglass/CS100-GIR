import common
import numpy as np

def grayscale(image_matrix):
    # Convert the image_matrix to a NumPy array
    image_array = np.array(image_matrix, dtype=np.uint8)

    # Initialize an empty grayscale matrix
    grayscale_matrix = np.zeros(image_array.shape[:2], dtype=np.uint8)

    # Loop through each pixel and calculate the average of color channels
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            pixel = image_array[i, j]
            # Calculate the average of color channels (R, G, B)
            pixel_mean = np.mean(pixel)
            # Set the grayscale_matrix value for the pixel
            grayscale_matrix[i, j] = int(pixel_mean)

    return grayscale_matrix

# Load the image
icespice = common.read_file("download.jpg")

# Apply the filter function to the image
gray_scale_icespice = grayscale(icespice)

# Write the modified image to a new file
common.write_file("grayicespice.jpg", gray_scale_icespice)

