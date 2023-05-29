# GIF_PROJ
The code combines multiple images from the specified folder into a single GIF file, resizing them to match the dimensions of the first image. The resulting GIF is saved with the specified frame delay.
The provided code allows you to create a GIF file by merging multiple images from a specified folder. It utilizes the os, imageio, PIL, and numpy libraries for file operations, GIF creation, image processing, and array manipulation, respectively.

The main function, merge_images_to_gif, takes three parameters:

folder_path: The path to the folder containing the images you want to merge.
gif_path: The desired output path for the resulting GIF file.
duration: The frame delay between each image in the GIF, specified in units of 1/100th of a second.
Within the function:

An empty list called images is created to store the image data.
Two variables, width and height, are initialized with default values of 0.
A loop iterates through the files in the specified folder_path.
For each image file, the code checks if it has either a ".png" or ".jpg" extension.
If the file matches the criteria, it is opened using the Image.open() function from the PIL library.
If it's the first image encountered (identified by first_image being None), the width and height are obtained from the first image using the .size attribute.
The subsequent images are then resized using the resize() method from PIL to match the dimensions of the first image.
Each resized image is converted to a numpy array using np.array() and added to the images list.
If an existing GIF file already exists at the gif_path, it is removed using os.remove() to ensure it can be overridden.
Finally, the imageio.mimsave() function is called to save the GIF file at the specified gif_path. It takes in the images list, duration for the frame delay, and other parameters required for the GIF creation.
Below the function definition, the code sets the folder_path, gif_path, and duration variables to the desired values. Then, the merge_images_to_gif function is invoked with these parameters to generate the GIF.

In summary, this code facilitates the merging of images from a folder into a single GIF file, with customizable frame delay between images. The resulting GIF can be saved at the specified output path.
