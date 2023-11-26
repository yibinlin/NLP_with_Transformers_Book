from PIL import Image, ImageDraw

def draw_black_rectangle(image, top_left, bottom_right):
    """
    Draw a black rectangle on the image.
    
    Parameters:
    - image: The image to draw on.
    - top_left: A tuple (x, y) for the top-left corner of the rectangle.
    - bottom_right: A tuple (x, y) for the bottom-right corner of the rectangle.
    """
    draw = ImageDraw.Draw(image)
    draw.rectangle([top_left, bottom_right], fill="black")

# Create an empty white image
width, height = 1024, 1024
white_color = (255, 255, 255)  # RGB for white
image = Image.new("RGB", (width, height), white_color)

# coordinates for the textbox
top_left_point = (375, 252)  # Replace with your coordinates
bottom_right_point = (648, 435)  # Replace with your coordinates
# top_left_point = (20, 20)  # Replace with your coordinates
# bottom_right_point = (1024, 1024)  # Replace with your coordinates


# Draw the black rectangle
draw_black_rectangle(image, top_left_point, bottom_right_point)

# Save the image
image.save('mask.png')
