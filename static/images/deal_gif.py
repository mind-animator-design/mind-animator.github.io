from PIL import Image, ImageSequence
import os

def set_gif_infinite_loop(input_path, output_path):
    with Image.open(input_path) as im:
        frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0)

def main(directory):
    i = 0
    for filename in os.listdir(directory):
        if filename.endswith(".gif") and 'infinite' not in filename:
            i += 1
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, "new_" + f'{i}.gif')
            set_gif_infinite_loop(input_path, output_path)

if __name__ == "__main__":
    dir_path = '.'  # 更改为你的文件夹路径
    main(dir_path)