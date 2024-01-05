from PIL import Image  # Correct the case for Image

def rotate_image(input_image_path, output_image_path, degrees):
    # Open the image
    image = Image.open(input_image_path)  # Use the correct case for Image

    # Rotate the image
    rotated_image = image.rotate(degrees, expand=True)

    # Save the rotated image
    rotated_image.save(output_image_path)

# Example usage
input_image_path = "redtrio.jpg"
output_image_path = "rotated_red_trio.jpg"
degrees = 90  # Replace with the desired rotation angle

rotate_image(input_image_path, output_image_path, degrees)
