import os
import imageio
from PIL import Image
import numpy as np

def merge_images_to_gif(folder_path, gif_path, duration):
    images = []
    first_image = None

    width = 0  # Initialize width with a default value
    height = 0  # Initialize height with a default value

    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            file_path = os.path.join(folder_path, filename)
            img = Image.open(file_path)
            if first_image is None:
                first_image = img
                width, height = first_image.size
            img = img.resize((width, height))
            images.append(np.array(img))

    if os.path.exists(gif_path):
        os.remove(gif_path)  # Remove existing GIF file if present

    imageio.mimsave(gif_path, images, duration=duration)

folder_path = "C://Users//nizar//Documents//projets//GIF_PROJ//Image"
gif_path = "C://Users//nizar//Documents//projets//GIF_PROJ//output.gif"
duration = 1000.0  # Frame delay in units of 1/100th of a second (1 second between frames)

merge_images_to_gif(folder_path, gif_path, duration)
