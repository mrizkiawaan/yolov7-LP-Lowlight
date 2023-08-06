from PIL import Image
import os

# Set the target width for resizing
target_width = 416

# Create a new folder for resized images
os.makedirs("resized_images", exist_ok=True)

# Path to the image folder
image_folder = os.path.join("LP_Lowlight_Dataset", "images")

# Get the list of image files in the image folder
image_files = os.listdir(image_folder)

# Resize each image and save it in the "resized_images" folder
for image_file in image_files:
    # Open the image using PIL
    image_path = os.path.join(image_folder, image_file)
    image = Image.open(image_path)

    # Calculate the target height based on the original aspect rati0-`o
    width, height = image.size
    target_height = int((target_width / width) * height)

    # Resize the image while maintaining the aspect ratio
    resized_image = image.resize((target_width, target_height), Image.LANCZOS)

    # Save the resized image in the "resized_images" folder
    resized_image_path = os.path.join("resized_images", image_file)
    resized_image.save(resized_image_path)

    # Close the image
    image.close()

print("Image resizing completed!")
