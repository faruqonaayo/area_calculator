import argparse

# initializing arguement parser
parser = argparse.ArgumentParser()


# adding arguements
parser.add_argument("--height", help="Add the height of the rectangle")
parser.add_argument("--width", help="Add the width of the rectangle")

args = parser.parse_args()


def calculate_area(height, width):
    """
    Calculates the area of a rectangle.

    Args:
        height (float or int): The height of the rectangle.
        width (float or int): The width of the rectangle.

    Returns:
        float or int: The calculated area of the rectangle.

    Raises:
        TypeError: If height or width is not a numeric type.

    Examples:
        >>> calculate_area(5, 10)
        50
        >>> calculate_area(3.5, 2)
        7.0
    """

    return height * width

if args.height and args.width:
    result = calculate_area(float(args.height),float(args.width))
    print(result)