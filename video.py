from PIL import Image
import os

image_folder = './pic'
output_gif = 'Riemann.gif'
def make_video(j):
    images = []
    for i in range(1, j):
        filename = f"{i:03d}.png"
        filepath = os.path.join(image_folder, filename)
        images.append(Image.open(filepath))
        print(filepath)
    images[0].save(output_gif,
            save_all=True,
            append_images=images[1:],
            duration=100,
            loop=0)

if __name__ == '__main__':
    make_video(30)