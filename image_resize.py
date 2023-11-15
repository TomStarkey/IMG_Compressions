import os
from PIL import Image


def get_file_names():
    for file in os.listdir(location):
        print("Reformating file")
        reformat_file(location, file)

# add conditional statement to compress smaller files at a smaller rate,
# and the larger files at a slightly larger rate.


def reformat_file(directory, file):
    # Create the full file path by joining the directory and file name
    file_path = os.path.join(directory, file)

    # Open the image file
    img = Image.open(file_path)

    # Calculate the height in a way that the aspect ratio is kept
    width_percent = (400 / float(img.size[0]))
    height_size = int((float(img.size[1]) * float(width_percent)))
    img = img.resize((400, height_size), Image.NEAREST)

    # Convert the image to JPEG
    img = img.convert("RGB")

    # Compress the JPEG image and save it
    img.save(f'{file}_compressed.jpeg', 'JPEG', quality=60)


location = 'C:\\Users\\Tom\\Desktop\\Python\\Image Resize'

get_file_names()
