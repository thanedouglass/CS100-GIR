import common

def invert_colors(image_matrix):
    max_pixel_value = 255

    # Convert the image_matrix to a NumPy array
    image_array = image_matrix

    inverted_matrix = []

    for row in image_array:
        inverted_row = []
        for pixel in row:
            inverted_pixel = [max_pixel_value - channel for channel in pixel]
            inverted_row.append(inverted_pixel)
        inverted_matrix.append(inverted_row)

    return inverted_matrix

# Load the image
bigred = common.read_file("bigred.jpg")

# Apply the filter function to the image
invert_filtered_image = invert_colors(bigred)

# Write the modified image to a new file
common.write_file("invertbigred.jpg", invert_filtered_image)

