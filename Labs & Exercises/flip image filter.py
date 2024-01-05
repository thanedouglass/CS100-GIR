import common

def flip(image_matrix):
    image_height = len(image_matrix)
    image_width = len(image_matrix[0])
    
    flipped_matrix = []

    # Reverse the order of rows to flip vertically
    for row in range(image_height - 1, -1, -1):
        flipped_matrix.append(image_matrix[row])

    # Reverse the order of columns to flip horizontally
    for row in range(image_height):
        flipped_row = flipped_matrix[row][::-1]
        flipped_matrix[row] = flipped_row

    return flipped_matrix

# Load the image
slime = common.read_file("slime.jpg")

# Apply the filter function to the image
flipped_image = flip(slime)

# Write the modified image to a new file
common.write_file("flipslime.jpg", flipped_image)
