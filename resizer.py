import glob
from PIL import Image
import os
import Augmentor

_FOLDER = "./data"

for img_file in glob.glob(_FOLDER + "/*.jpg"):
	img = Image.open(img_file)
	img = img.resize((200, 200), Image.ANTIALIAS)
	filename = img_file.split("/")[-1]

	dst_name = os.path.join("./ResizeData", filename)
	img.save(dst_name)

_THUMB_FOLDER = "./ResizeData"
_OUTPUT_FOLDER_flip = "../flip_output"
p_flip = Augmentor.Pipeline(_THUMB_FOLDER, _OUTPUT_FOLDER_flip)
p_flip.flip_left_right(probability=1.0)
p_flip.sample(1099)