import common
import numpy as np
import copy

def blur_image(image_matrix, kernel_size=3):
    # Convert the input image list to a NumPy array
    image_matrix = np.array(image_matrix)

    # Create a deep copy of the original image
    blurred_image = copy.deepcopy(image_matrix)

    # Define the kernel for blurring (box filter)
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)

    # Get the dimensions of the image
    height, width, num_channels = image_matrix.shape

    # Iterate through the image and apply the blurring filter
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            for c in range(num_channels):
                # Calculate the weighted average for the pixel
                pixel_sum = 0.0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        pixel_sum += image_matrix[i + x, j + y, c] * kernel[x + 1, y + 1]
                blurred_image[i, j, c] = pixel_sum

    return blurred_image

# Load the image
image = common.read_file("redtrio.jpg")

# Apply the blurring function to the image
blurred_image = blur_image(image, kernel_size=3)

# Save the blurred image
common.write_file("blurredredtrio.jpg", blurred_image)


