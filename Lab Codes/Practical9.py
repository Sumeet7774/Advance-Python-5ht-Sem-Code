from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np

# Load and display the image
def load_and_display_image(image_path):
    img = Image.open(image_path)
    plt.imshow(img)
    plt.axis('off')  # Hide axes
    plt.show()

# Apply Gaussian blur and display
def apply_gaussian_blur(image_path):
    img = Image.open(image_path)
    blurred_img = img.filter(ImageFilter.GaussianBlur(radius=5))
    blurred_img.show()

# Convert to grayscale and display
def convert_to_grayscale(image_path):
    img = Image.open(image_path)
    grayscale_img = img.convert("L")  # "L" mode is grayscale
    grayscale_img.show()

# Show histogram for the image
def show_histogram(image_path):
    img = Image.open(image_path)
    img_arr = np.array(img)

    colors = ('r', 'g', 'b')
    plt.figure()

    for i, color in enumerate(colors):
        plt.hist(img_arr[:, :, i].ravel(), bins=256, color=color, alpha=0.6, label=color)

    plt.legend()
    plt.title('Histogram for RGB Channels')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.show()

# Example usage
image_path = r'G:\Codes\College\Sem 5\Advance Python\Lab Codes\practical9 image.jpeg'

# Sequential operations
load_and_display_image(image_path)  # Step 1: Load and display image
input("Press Enter to apply Gaussian blur...")  # Wait for user input

apply_gaussian_blur(image_path)  # Step 2: Apply blur
input("Press Enter to convert to grayscale...")  # Wait for user input

convert_to_grayscale(image_path)  # Step 3: Convert to grayscale
input("Press Enter to show histogram...")  # Wait for user input

show_histogram(image_path)  # Step 4: Show histogram