import imageio.v2 as imageio
import numpy as np

def read_file(file_path):
    """Gets the pixels of an image.

    Args:
    file_path: Name of the file to read. Paths relative to the home directory or absolute paths are accepted.

    Returns:
    The output matrix which has the following format.
    [
        row1 -->[[r,g,b], [r, g, b]],
        row2 -->[[r,g,b], [r, g, b]]
    ]
    """
    try:
        return imageio.imread(file_path).tolist()
    except Exception as e:
        print(e)
        return []

def write_file(file_name, image_matrix):
    """Write the matrix to a file. This will not overwrite a file that already exists.

    Args:
    file_name: Name of the file. Accepts paths relative to home, or absolute paths.
    image_matrix: An array with the following format.
    [
        row1 -->[[r,g,b], [r, g, b]],
        row2 -->[[r,g,b], [r, g, b]]
    ]
    """
    im = np.array(image_matrix).astype(np.uint8)
    imageio.imwrite(file_name, im)

