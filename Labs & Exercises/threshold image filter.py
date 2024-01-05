import common
import numpy as np

def threshold(image_matrix, red_min, red_max, green_min, green_max, blue_min, blue_max):
    # Convert the input image list to a NumPy array
    image_matrix = np.array(image_matrix)

    # Get the dimensions of the image
    num_rows, num_cols, num_channels = image_matrix.shape

    # Iterate through the image and apply the thresholding
    for i in range(num_rows):
        for j in range(num_cols):
            pixel = image_matrix[i, j]
            red, green, blue = pixel[0], pixel[1], pixel[2]
            
            # Check if the pixel values are within the specified thresholds
            if (
                red_min <= red <= red_max and
                green_min <= green <= green_max and
                blue_min <= blue <= blue_max
            ):
                # Pixel is within the threshold, keep the original color
                pass
            else:
                # Pixel is outside the threshold, set it to black
                image_matrix[i, j] = [0, 0, 0]

    return image_matrix

# Example usage with custom threshold values
image = common.read_file("redtrio.jpg")
# Define your threshold values here
red_min = 100
red_max = 255
green_min = 0
green_max = 150
blue_min = 0
blue_max = 150

# Apply the threshold function to the image
thresholded_image = threshold(image, red_min, red_max, green_min, green_max, blue_min, blue_max)

# Save the thresholded image
common.write_file("thresholded_redtrio.jpg", thresholded_image)

