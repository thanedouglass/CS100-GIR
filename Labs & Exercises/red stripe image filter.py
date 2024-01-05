import common

def red_stripe(image_matrix, stripe_height=50, gap_height=50):
    image_height = len(image_matrix)
    image_width = len(image_matrix[0])
    current_stripe = 0

    for row in range(image_height):
        # Check if we are in a stripe
        if current_stripe < stripe_height:
            # for each row, go through each column
            for col in range(image_width):
                image_matrix[row][col][0] = 255  # Set red component to 255
        current_stripe = (current_stripe + 1) % (stripe_height + gap_height)
    
    return image_matrix

# Load the image
hellcats = common.read_file("hellcats.jpg")

# Apply the filter function to the image
red_filtered_image = red_stripe(hellcats)

# Write the modified image to a new file
common.write_file("hellcats_with_red_stripes.jpg", red_filtered_image)

